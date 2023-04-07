from sqlalchemy import create_engine, text

dbConnectionString = "mysql+pymysql://z90snti9zhc76auts0p1:pscale_pw_aWeY7W64cJqo3nQ0g0FaNl83DlYgWRRb2Lo9fs9A5xL@aws.connect.psdb.cloud/panther-carrers-database?charset=utf8mb4"

engine = create_engine(dbConnectionString,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)

def loadJobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for job in result.all():
      jobs.append(dict(job._mapping))
    return jobs