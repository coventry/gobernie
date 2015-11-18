import csv

def mkdir_safe(p):
    assert not os.system('mkdir -p ' + p)

counties = [l.strip() for l in open('~/bernie/outreach/gobernie/counties.txt')]

fields = '''COUNTY_NUMBER,LAST_NAME,FIRST_NAME,MIDDLE_NAME,SUFFIX,DATE_OF_BIRTH,PARTY_AFFILIATION,RESIDENTIAL_ADDRESS1,RESIDENTIAL_SECONDARY_ADDR,RESIDENTIAL_CITY,RESIDENTIAL_STATE,RESIDENTIAL_ZIP,RESIDENTIAL_ZIP_PLUS4,RESIDENTIAL_COUNTRY,RESIDENTIAL_POSTALCODE,MAILING_ADDRESS1,MAILING_SECONDARY_ADDRESS,MAILING_CITY,MAILING_STATE,MAILING_ZIP,MAILING_ZIP_PLUS4,MAILING_COUNTRY,MAILING_POSTAL_CODE,CITY,TOWNSHIP,VILLAGE,PRIMARY-05/07/2013,PRIMARY-09/10/2013,PRIMARY-10/01/2013,PRIMARY-05/06/2014,PRIMARY-05/05/2015
'''.strip()

outdir = '/play/coventry/bernie/by-county-zip'
mkdir_safe(outdir)

def get_outfile((countynum, _zip)):
    county = counties[int(countynum)-1]
    mkdir_safe(os.path.join(outdir, county))
    outpath = os.path.join(outdir, county, '%s.csv' % _zip)
    if not os.path.exists(outpath):
        print >> open(outpath, 'w'), fields
    else:
        assert open(outpath).readline().strip() == fields
    return open(outpath, 'a')

outfiles = ddict(get_outfile)

def get_data(path):
    f = open(path)
    headers = csv.reader(f).next()
    for rownum, row in enumerate(csv.DictReader(f, headers)):
        if rownum % 10000 == 0:
            print rownum
        pathinfo = row['COUNTY_NUMBER'], row['RESIDENTIAL_ZIP']
        outfile = outfiles[pathinfo] = outfiles[pathinfo] if pathinfo in outfiles else get_outfile(pathinfo)
        print >> outfile, ','.join(row[f] for f in fields.split(','))

for p in glob('/play/coventry/bernie/SWVF_*.TXT'):
    get_data(p)

for outfile in outfiles.values():
    outfile.close()
