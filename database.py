from sqlalchemy import create_engine, text

dbConnectionString = "mysql+pymysql://svnobvpui6klga3er0xi:pscale_pw_doutfYsjXOe0R9GsaAfNoSRBs3GuNe3a7OfgS7PoIOI@aws.connect.psdb.cloud/panther-carrers-database?charset=utf8mb4"

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
print(loadJobs())
