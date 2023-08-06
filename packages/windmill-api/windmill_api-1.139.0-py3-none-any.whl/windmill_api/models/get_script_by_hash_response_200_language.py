from enum import Enum


class GetScriptByHashResponse200Language(str, Enum):
    PYTHON3 = "python3"
    DENO = "deno"
    GO = "go"
    BASH = "bash"
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    BIGQUERY = "bigquery"
    GRAPHQL = "graphql"
    NATIVETS = "nativets"
    BUN = "bun"

    def __str__(self) -> str:
        return str(self.value)
