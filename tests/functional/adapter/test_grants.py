import pytest
from dbt.tests.adapter.grants.test_incremental_grants import BaseIncrementalGrants
from dbt.tests.adapter.grants.test_invalid_grants import BaseInvalidGrants
from dbt.tests.adapter.grants.test_model_grants import BaseModelGrants
from dbt.tests.adapter.grants.test_seed_grants import BaseSeedGrants
from dbt.tests.adapter.grants.test_snapshot_grants import BaseSnapshotGrants


class TestIncrementalGrantsSQLServer(BaseIncrementalGrants):
    pass


@pytest.mark.only_with_profile("user", "ci_sql_server")
class TestInvalidGrantsSQLServer(BaseInvalidGrants):
    def grantee_does_not_exist_error(self):
        return "Cannot find the user"

    def privilege_does_not_exist_error(self):
        return "Incorrect syntax near"


@pytest.mark.skip_profile("user", "ci_sql_server")
class TestInvalidGrantsSQLServerAzure(BaseInvalidGrants):
    def grantee_does_not_exist_error(self):
        return "Principal 'invalid_user' could not be found"

    def privilege_does_not_exist_error(self):
        return "Incorrect syntax near"


class TestModelGrantsSQLServer(BaseModelGrants):
    pass


class TestSeedGrantsSQLServer(BaseSeedGrants):
    pass


class TestSnapshotGrantsSQLServer(BaseSnapshotGrants):
    pass
