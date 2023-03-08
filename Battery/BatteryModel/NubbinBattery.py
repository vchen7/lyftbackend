from Battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.nubbin_need = 4

    def needs_service(self):
        date_need = self.last_service_date.replace(year=self.last_service_date.year + self.nubbin_need)
        if date_need < self.current_date:
            return True
        else:
            return False