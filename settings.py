import argparse
import logging

def setup_parser():
    parser = argparse.ArgumentParser(description='Обработка CSV файлов с экономическими данными')
    parser.add_argument('--files', nargs='+', required=True, help='Список CSV файлов для обработки')
    parser.add_argument('--report', help='Имя отчета')
    args = parser.parse_args()
    return args.files, args.report

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename='app.log',
        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)