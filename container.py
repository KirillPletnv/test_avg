
class Container:
    def __init__(self, file_list, logger, report_type='average-gdp'):
        self.file_list = file_list
        self._storage = {}
        self.logger = logger
        self.report_type = report_type  # сохраняем
        self._processor = None
        self.get_processor()

    @property
    def storage(self):
        return self._storage

    def get_processor(self):
        if self._processor is None:
            from service import FileProcessor
            self._processor = FileProcessor(
                file_list=self.file_list,
                storage=self._storage,
                logger=self.logger,
                report_type=self.report_type
            )
            self._processor.run_process()
        return self._processor