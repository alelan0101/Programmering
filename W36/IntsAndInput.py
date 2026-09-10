from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def IntOnlyInput(query: str) -> int:
    while True:
        try:
            result = input(query)
            return int(result)
        except ValueError:
            print("Det er desvaerre ikke et nummer, proev igen!")

yearOfBirth = IntOnlyInput("What year were you born?")
monthOfBirth = IntOnlyInput("Which month were you born?")
dayOfBirth = IntOnlyInput("Which day of the month were you born?")

datetimeBirth = datetime(year=yearOfBirth, day=dayOfBirth, month=monthOfBirth, tzinfo=ZoneInfo("Europe/Copenhagen"));
datetimeInOneYear = datetime.now(tz=ZoneInfo("Europe/Copenhagen")) + timedelta(days=365)

daysOld = (datetimeInOneYear - datetimeBirth).days
yearsOld = int(daysOld / 365)
remainingDays = daysOld % 365

print("The user will be " + str(yearsOld) + " years and " + str(remainingDays) + " days old in one year")
