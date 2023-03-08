from Battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.spindler_need = 3

    def needs_service(self):
        date_need = self.last_service_date.replace(year=self.last_service_date.year + self.spindler)
        if date_need < self.current_date:
            return True
        else:
            return False