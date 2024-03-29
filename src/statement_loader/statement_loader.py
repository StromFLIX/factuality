from enum import Enum
from statement_loader.txt_loader.txt_loader import TxtLoader

# Define an enum for source types
class SourceType(Enum):
    TXT = 'txt'
    GITHUB_PR_COMMENT = 'github_pr_comment'
    TWITTER = 'twitter'

# Implementation of the StatementLoader class
class StatementLoader:
    def load_statement(self, source_type, source):
        if source_type == SourceType.TXT:
            return TxtLoader().load(source)
        elif source_type == SourceType.GITHUB_PR_COMMENT:
            raise NotImplementedError("Loader for GitHub PR comments is not implemented yet.")
        elif source_type == SourceType.TWITTER:
            raise NotImplementedError("Loader for Twitter is not implemented yet.")
        else:
            raise ValueError(f"No loader found for source type: {source_type}")
