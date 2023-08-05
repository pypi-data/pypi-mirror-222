from alembic import command
from alembic.config import Config
from sqlalchemy import URL
from pathlib import Path


class Alembic:
    def __init__(self, database_url: URL, db: str):
        current_file = Path(__file__)
        self.alembic_folder = current_file.parent
        self.alembic_setup(database_url.render_as_string(hide_password=False), db)

    def alembic_setup(
        self,
        database_url: str,
        db: str,
    ):
        # logger.get_file_logger(
        #     base_path=log_path / "alembic",
        #     name="root",
        #     level=logger.WARNING,
        #     stderr_level=logger.WARNING
        # )

        # logger.get_file_logger(
        #     base_path=log_path / "alembic",
        #     name="sqlalchemy",
        #     level=logger.WARNING,
        #     stderr_level=logger.WARNING,
        # )

        # logger.get_file_logger(
        #     base_path=log_path / "alembic",
        #     name="alembic",
        #     level=logger.INFO,
        #     stderr_level=logger.INFO,
        # )

        # Create an Alembic configuration object
        self.alembic_cfg = Config()  # conf modo dict

        # Set the database URL
        self.alembic_cfg.set_main_option(
            "sqlalchemy.url", database_url.replace("%", "%%")
        )

        _versions_location = self.alembic_folder / db / "versions"
        self.alembic_cfg.set_main_option(
            "version_locations", str(_versions_location.absolute())
        )

        _script_location = self.alembic_folder / db
        self.alembic_cfg.set_main_option(
            "script_location", str(_script_location.absolute())
        )

        self.alembic_cfg.set_main_option(
            "file_template",
            "%%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s",
        )

        self.alembic_cfg.set_main_option("prepend_sys_path", ".")

        self.alembic_cfg.set_main_option("version_path_separator", "os")

    # Run the revision for the database
    def create_revision(self, message: str, autogenerate: bool):
        command.revision(
            autogenerate=autogenerate,
            config=self.alembic_cfg,
            message=message,
            head="head",
        )

    # Upgrade revision
    def upgrade_revision(self, rev: str):
        command.upgrade(self.alembic_cfg, rev)

    # Downgrade revision
    def downgrade_revision(self, rev: str):
        command.downgrade(self.alembic_cfg, rev)

    # Stamp version (point a revision as head)
    def stamp_revision(self, rev: str, purge: bool):
        command.stamp(self.alembic_cfg, rev, purge=purge)

    # Check current version of database
    def check_current(self):
        command.current(self.alembic_cfg)

    def history(self):
        command.history(self.alembic_cfg)
