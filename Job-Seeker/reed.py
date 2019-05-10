''' Communicates with the reed api

'''

API_key= '3dbd30fd-117e-42a5-ac4f-2f1908c082ed'

Access_format = 'https: // www.reed.co.uk/api/{version number}/jobs/{Job Id} e.g. https: // www.reed.co.uk/api/1.0/jobs/132'
search_format = 'https://www.reed.co.uk/api/{versionnumber}/search?keywords={keywords}&locationName={locationName}&employerId={employerId}&distanceFromLocation={distanceinmiles}'

job_will_return= ["job_id","employer_id","employer_name",
                    "employer_profile_id","job_title","description",
                    "location_name","minimum_salary","maximum_salary"]