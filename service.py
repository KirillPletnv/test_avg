from repository import Repository
from tabulate import tabulate

#Вызывается в файл процесоре если выбран этот тип отчета в report_type
class AverageGdpProcessor:
    def __init__(self, gen_obj, storage):
        self.gen_obj = gen_obj
        self.storage = storage
        self.process()

    def process(self):
        for i in self.gen_obj:
            country = i[0]
            value = float(i[2])
            if country in self.storage:
                self.storage[country][0] += value
                self.storage[country][1] += 1
            else:
                self.storage[country] = [value, 1]


class FileProcessor:
    def __init__(self, file_list, storage=None, logger=None, report_type='average-gdp'):
        self.file_list = file_list
        self.processed_count = 0
        self.failed_count = 0
        self.storage = storage
        self.logger = logger
        self.report_type = report_type

    @classmethod
    def process_all(cls, file_list):
        processor = cls(file_list)
        return processor.run_process()

    def run_process(self):
        for filename in self.file_list:
            self._process_single_file(filename)

        self.logger.info(f"Обработка завершена. Успешно: {self.processed_count}, Ошибок: {self.failed_count}")
        return self.processed_count, self.failed_count

    def _process_single_file(self, filename):
        try:
            gen = Repository(filename)

            if self.report_type == 'average-gdp':
                AverageGdpProcessor(gen(), self.storage)

            self.processed_count += 1
            self.logger.info(f"Обработан файл: {filename}")
        except FileNotFoundError:
            self.failed_count += 1
            self.logger.error(f"Файл {filename} не найден, пропускаем")
        except Exception as e:
            self.failed_count += 1
            self.logger.error(f"Ошибка при обработке {filename}: {e}")

    def get_stats(self):
        return {'total': len(self.file_list),
                'processed': self.processed_count,
                'failed': self.failed_count}



class ReportViewer:
    def __init__(self, data, report_type='average-gdp', logger=None):
        self.data = data
        self.logger = logger
        self.report_type = report_type

    def display(self):
        if not self.data:
            msg = "Нет данных для отображения"
            if self.logger:
                self.logger.warning(msg)
            else:
                print(msg)
            return

        # Выбираем формат отчета
        if self.report_type == 'average-gdp':
            self._display_avg_gdp()
        # сюда добавлять новые

    def _display_avg_gdp(self):
        table_data = []
        for country, values in self.data.items():
            avg = values[0] / values[1]
            avg_rounded = round(avg, 2)
            table_data.append([country, avg_rounded])
        table_data.sort(key=lambda x: x[1], reverse=True)
        print(tabulate(
            table_data,
            headers=["Country", "Avg GDP"],
            tablefmt="grid",
            floatfmt=".2f",
            numalign="right"))

    def __call__(self):
        return self.display()

