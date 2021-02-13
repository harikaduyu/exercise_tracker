from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Routine


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as td
    # filters routines by day
    def formatday(self, day, routines):
        routines_per_day = routines.filter(date_created__day=day)
        d = ''
        for routine in routines_per_day:
            d += f"<li> {routine.exercise.name} </li>"

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as tr
    def formatweek(self, theweek, routines):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, routines)
        return f"<tr> {week} </tr>"

    # formats a month as table
    # filter routines by year and month
    def formatmonth(self, withyear=True):
        routines = Routine.objects.filter(
            date_created__year=self.year, date_created__month=self.month)
        calendar_table = f"<table border='0' cellpadding='0' cellspacing='0' class='calendar' >\n"
        calendar_table += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        calendar_table += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            calendar_table += f"{self.formatweek(week,routines)}\n"
        calendar_table += "</table>"
        return calendar_table
