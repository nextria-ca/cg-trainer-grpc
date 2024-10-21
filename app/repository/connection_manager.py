from contextlib import asynccontextmanager
from sql_alchemy.connection import get_session
from custom_logger import logger


class ConnectionManager:
    def __init__(self):
        self.current_session = None
        self.transaction_started = False

    async def start_transaction(self, connection=get_session()):
        self.current_session = connection
        self.transaction = await self.current_session.__aenter__()
        self.transaction_started = True
        logger.info("Transaction started")

    async def end_transaction(self, commit=True):
        if self.current_session and self.transaction_started:
            try:
                if commit:
                    logger.info("Committing transaction")
                    await self.transaction.commit()
                else:
                    logger.info("Rolling back transaction")
                    await self.transaction.rollback()
            finally:
                await self.current_session.__aexit__(None, None, None)
                self.transaction_started = False
                self.current_session = None

    @asynccontextmanager
    async def get_session(self):
        if self.transaction_started:
            logger.info("Using transaction")
            yield self.transaction
        else:
            async with get_session() as session:
                yield session