class App:
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION: int
    root_path: str
    name: str


class PostgreSQLConfig:
    host: str
    port: int
    username: str
    password: str | None
    database: str
    thread_connection_pool_size: int


class DatabaseConfig:
    app: PostgreSQLConfig


class Settings:
    app: App
    database: DatabaseConfig
