# vim :set fileencoding=utf-8
import nose.tools as n
import StringIO
import lib

def test_chunk():
    fp = StringIO.StringIO('''
Chapter 10.32

STOPPING, STANDING AND PARKING IN
SPECIFIC STREETS AND PLACES

Sections:
10.32.010 Parking of vehicles in municipal

parking lots controlled by coin-
operated mechanical entrance
and exit gates—Tampering with
gates prohibited.

Parking areas for official cars at
City Hall.

Parking area for official cars at
Police Administration Building.
Parking area for ofﬁcial cars at
the Port of Oakland.

Parking area for ofﬁcial cars at
the City Hall Annex Building.
Parking area for official cars at
the Administrative Annex
Building (659 - 14th Street).
Parking area for official cars at
the Oakland Detention Facility
Building.

Parking areas for official cars at
the Alameda County
Courthouse (1225 Fallon
Street).

Parking area for official cars at
the Kaiser Center Building.
Parking for official cars of
Oakland Police Department and
county of Alameda.

Parking for official cars of the
GSA Federal Protective Service.
Parking area for police service
vehicles of the Oakland Police
Department and the Bay Area
Rapid Transit District.

Parking area for Oakland Fire
Department vehicles.

Parking area for county cars.

10.32.020

10.32.030

10.32.040

10.32.050

10.32.060

l0.32.070

10.32.080

10.32.090

10.32.100

10.32.110

10.32.120

10.32.130

10.32.140

506-l

10.32.010

10.32.150 Parking area for U.S. Mail
vehicles.

10.32.160 Parking for Consuls and Vice
Consuls.

10.32.170 Parking area for ofﬁce of parks
and recreation vehicles.

10.32.180 Press parking privileges.

10.32.190 Parking restrictions in Port of
Oakland Outer Harbor
Terminal Area.

10.32.200 Citations and arrests.

10.32.010 Parking of vehicles in municipal

parking lots controlled by coin-
operated mechanical entrance and
exit gates——Tampering with gates
prohibited.

A. It is unlawful for any person to park, or at-
tempt to park, any vehicle in any municipal parking
lot or area, entrance and exit to which is controlled
by mechanical gates. without entering said lot
through said entrance gate and without depositing
immediately prior to such entrance. one or more
coins of the United States in the coin receptacle pro-
vided therefor in accordance with the directions ap-
pearing on, near or adjacent to said mechanical en-
trance gate.

B. It is unlawful for any person to deface, injure,
tamper with, or wilfully break, destroy or impair the
usefulness or normal operation of any mechanical
gate, or its appurtenances, which control ingress to

and egress from any municipal parking lot. (Prior
traffic code §§ 127.1, 127.2)

10.32.020

Parking areas for official cars at
City Hall.

The west side of Washington Street from 14th
Street to eighty (80) feet northerly therefrom, the
south side of 15th Street from Washington Street to a
point seventy (70) feet westerly therefrom, and the
north side of 14th Street from the west line of Wash-
ington Street to a point two hundred (200) feet west-
erly therefrom are set aside and reserved for parking
official cars between the hours of eight a.m.

(Oakland Supp No 19, 1-03)
''')
    observed = lib.chunk(fp)
    expected_keys = {
        '10.32',
        '10.32.010',
        '10.32.150',
        '10.32.160',
        '10.32.170',
        '10.32.180',
        '10.32.190',
        '10.32.200',
        '10.32.010',
        '10.32.020',
    }
    n.assert_true(expected_keys.issubset(observed.keys()))

def test_network():
    observed = set(lib.network({'8.03.050': 'Also see OMC Section 5.34.051.)', '5.34.051': 'pursuant to Section 5.34.080.'}))
    expected = {('8.03.050','5.34.051'),('5.34.051','5.34.080')}
    n.assert_set_equal(observed, expected)
