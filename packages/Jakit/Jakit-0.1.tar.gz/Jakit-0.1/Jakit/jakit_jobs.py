import pymongo
from bson.objectid import ObjectId
from Dager.dager_data import Database

Dager_client = "mongodb://DaggerData_rw:eEsQcKvMgKfH5Di@p1ir1mon019.ger.corp.intel.com:7174,p2ir1mon019.ger.corp.intel.com:7174,p3ir1mon019.ger.corp.intel.com:7174/DaggerData?ssl=true&replicaSet=mongo7174"
Dager_conn = 'DaggerData'
Jobs_status_coll = 'Jobs'

ConnectionStringDager = pymongo.MongoClient(Dager_client)
DatabaseDager = ConnectionStringDager[Dager_conn]
CollectionJobs = DatabaseDager[Jobs_status_coll]

class JakitJobs:
    """Jobs class"""

    def __init__(self):
        '''Initialize jobids'''
        # Convert jobids to ObjectIds
        # self.jobids = [ObjectId(jobid) for jobid in jobids]

    def get_jobs(self,jobids):
        """ Read from Mongo and Store into DataFrame """

        jobs = CollectionJobs.find({"_id": {"$in": jobids}})
        list_jobs = list(jobs)

        return list_jobs
    
    def job_info(self,jobids,indicator_names):
        jobids = [ObjectId(jobid) for jobid in jobids]
        dager_data = Database()
        jobs_info = self.get_jobs(jobids)


        for job in jobs_info:
            # Only keep indicators where 'Name' matches 'indicator_name'
            job['Indicators'] = [ind for ind in job['Indicators'] if ind['Name'] in indicator_names]

            lot = job['Lot']
            operation = job['Operation']
            wfrs = job['Wafers']

            # Initialize 'Data' field in job
            job['Data'] = {}

            for indicator in job['Indicators']:
                indicator_name = indicator['Name']
                for wfr in wfrs:
                    df_data = dager_data.pull_data(lot, indicator_name, operation, wfr, output_format='dataframe')

                    # Store dataframe in 'Data' field under corresponding wafer
                    if wfr not in job['Data']:
                        job['Data'][wfr] = {}
                    job['Data'][wfr][indicator_name] = df_data

        return jobs_info
    
# jobids = ['64c8b660737dbc28fa09c61a','64c8b66a737dbc28fa09c61b','64c8b677737dbc28fa09c61c']
# jobs_info = JakitJobs(jobids).get_jobs()
# print(jobs_info)