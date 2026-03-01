from service import ReportViewer
from container import Container
from settings import setup_parser, setup_logging

logger = setup_logging()

if __name__ == "__main__":
    files, report_name = setup_parser()
    report_type = report_name if report_name else 'average-gdp'

    container = Container(files, logger, report_type=report_type)
    ReportViewer(container.storage, report_type=report_type, logger=logger)()