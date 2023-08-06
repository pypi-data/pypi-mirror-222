from redis import asyncio as aioredis
import asyncio
import time


class AsyncRedis:
    def __init__(self, host, port, password, db, pool_size: int = 10):
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.pool_size = pool_size
        self.redis_store = None

    async def initialize(self):
        pool = aioredis.ConnectionPool(
            host=self.host,
            port=self.port,
            db=self.db,
            password=self.password,
            max_connections=self.pool_size,
            encoding="utf-8",
            decode_responses=True,
        )
        self.redis_store = aioredis.Redis(connection_pool=pool)

    async def close(self):
        await self.redis_store.close()
        self.redis_store = None

    async def get_redis(self):
        if self.redis_store is None:
            await self.initialize()
        else:
            try:
                await self.redis_store.ping()
            except (aioredis.ConnectionError, aioredis.TimeoutError):
                await self.initialize()
        return self.redis_store

    async def set(self, key: str, value: str):
        conn = await self.get_redis()
        await conn.set(key, value)

    async def get(self, key: str) -> str:
        conn = await self.get_redis()
        return await conn.get(key)

    async def incr(self, key):
        conn = await self.get_redis()
        await conn.incr(key)

    async def zremrangebyscore(self, key, min_score, max_score):
        conn = await self.get_redis()
        await conn.zremrangebyscore(key, min_score, max_score)

    async def zcard(self, key):
        conn = await self.get_redis()
        await conn.zcard(key)

    async def zadd(self, key, mapping):
        conn = await self.get_redis()
        await conn.zadd(key, mapping)

    async def expire(self, key, seconds):
        conn = await self.get_redis()
        await conn.expire(key, seconds)

    async def publish(self, key: str, value: any):
        conn = await self.get_redis()
        await conn.publish(key, value)

    async def subscribe(self, key: str, handleFunc):
        conn = await self.get_redis()
        pubsub = conn.pubsub()
        await pubsub.subscribe(key)
        asyncio.get_event_loop().create_task(handleFunc(pubsub))

    async def wait(self, key, value):
        conn = await self.get_redis()
        pubsub = conn.pubsub()
        await pubsub.subscribe(key)
        while True:
            d1, d2, data = await pubsub.parse_response()
            if data == value:
                break

    async def acquire_lock(self, key, expiry_time):
        conn = await self.get_redis()
        end_time = time.time() + expiry_time
        lock_acquired = await conn.set(key, end_time, ex=expiry_time, nx=True)
        if not lock_acquired:
            current_value = await conn.get(key)
            if current_value and time.time() > float(current_value):
                previous_value = await conn.getset(key, end_time)
                if previous_value and previous_value == current_value:
                    lock_acquired = True
        return bool(lock_acquired)


