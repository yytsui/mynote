#http://agiliq.com/blog/2009/02/understanding-datetime-tzinfo-timedelta-amp-timezo/
#http://pytz.sourceforge.net/
# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

from datetime import datetime

# <codecell>

dt = datetime.now()

# <codecell>

dt

# <codecell>

dt.tzinfo

# <codecell>

print dt.tzinfo

# <codecell>

from pytz import timezone

# <codecell>

import pytz

# <codecell>

utc = pytz.utc

# <codecell>

pacific = timezone('Canada/Pacific')

# <codecell>

dt_aware = dt.replace(tzinfo=pacific)

# <codecell>

dt_aware

# <codecell>

dt_aware.utcoffset()

# <codecell>

dt_utc = dt_aware.astimezone(utc)

# <codecell>

#dt_aware.astimezone(utc).strftime("%Y-%m-%d %H:%M:%S %Z")
print dt_aware.strftime("%Y-%m-%d %H:%M:%S %Z")
print dt_utc.strftime("%Y-%m-%d %H:%M:%S %Z")


# <codecell>


