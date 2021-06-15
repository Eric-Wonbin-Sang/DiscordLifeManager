
class WeightRecord:

    def __init__(self, dt, weight_lb, last_weight_record=None):

        self.dt = dt
        self.weight_lb = weight_lb
        self.weight_kg = round(self.weight_lb / 2.20462, 2)

        self.last_weight_record = last_weight_record
        self.weight_lb_delta = self.get_weight_lb_delta()

    def get_weight_lb_delta(self):
        if self.last_weight_record:
            return round(self.weight_lb - self.last_weight_record.weight_lb, 2)
        return None

    def get_data_row(self):
        return [
            self.dt.strftime("%Y/%m/%d %H:%M %p"),
            self.weight_lb,
            self.weight_kg,
            self.weight_lb_delta
        ]

    def add_to_google_sheet(self, sheet):
        sheet.append_row(self.get_data_row(), value_input_option='USER_ENTERED')

    def __str__(self):
        return "WeightRecord | dt={}, weight_lb={}, weight_kg={}, weight_lb_delta={}".format(
            self.dt,
            self.weight_lb,
            self.weight_kg,
            self.weight_lb_delta
        )
