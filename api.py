###----------[ THE REQUIRED MODULES ]---------- ###
import requests,random,uuid,string,hashlib
ses=requests.Session()

###----------[ GENERATING DATA ]---------- ###
# Hash : hashlib.md5(hashlib.sha1(str(int(round(time.time()))).encode()).hexdigest().encode()).hexdigest()
# Hash Result = str(Hash[0:8])+"-"+str(Hash[4:8])+"-"+str(Hash[4:12])+"-"+str(Hash[4:16])+"-"+str(Hash[12:20])
# Uuid : str(uuid.uuid4())
### Recommended Use Uuid ###

###----------[ APP ID AND TOKEN ]---------- ###
# Ads Manager Android : 438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28
# Facebook Android : 350685531728|62f8ce9f74b12f84c123cc23437a4a32
# Facebook iPhone : 6628568379|c1e620fa708a1d5696fb991c1bde5662
# Ads Manager App for iOS : 1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae
# Instagram Web : 1217981644879628|65a937f07619e8d4dce239c462a447ce
# Instagram Android : 567067343352427|f249176f09e26ce54212b472dbab8fa8
### Example : App ID|Token/Sig ###

###----------[ URL FOR REQUESTS POST ]---------- ###
# Api : https://api.facebook.com/auth/login
# B-Api : https://b-api.facebook.com/auth/login
# Graph : https://graph.facebook.com/auth/login/
# B-Graph : https://b-graph.facebook.com/auth/login
### In The Url Can Also Use auth.login With The Condition That Headers Must Be Added {"method":"auth.login"} ###

###----------[ EXAMPLE USER AGENT AND PARSER ]---------- ###
# User Agent : Davik/2.1.0 (Linux; U; Android 4.0.0; Infinix X682B Build/Build/QP1A.190711.020; wv) [FBAN/AndroidSampleApp;FBAV/348.719.618.179;FBLC/en_US;FBBV/709835163;FBCR/Zong;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X682B;FBSV/12.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1216};FB_FW/1;]
# Device : Infinix X682B
# Versi Android/OS : 4.0.0
# App Version : 348.719.618.179

### ↓↓↓↓↓↓[ FOR EXAMPLE CODE TO REQUESTS ]↓↓↓↓↓↓ ###

###----------[ DATA FOR REQUESTS]---------- ###
data = {
	"email": email, # --> Email Facebook
	"password": pw, # --> Password Facebook
	"adid": str(uuid.uuid4()),
	"device_id": str(uuid.uuid4()),
	"family_device_id": str(uuid.uuid4()),
	"session_id": str(uuid.uuid4()),
	"advertiser_id": str(uuid.uuid4()),
	"reg_instance": str(uuid.uuid4()),
	"machine_id": "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24)),
	"locale": "en_US", # --> From Parsing User Agent
	"country_code": "US", # --> From Parsing User Agent
	"client_country_code": "US", # --> From Parsing User Agent
	"cpl": "true",
	"source": "login",
	"format": "json",
	"credentials_type": "password",
	"error_detail_type": "button_with_disabled",
	"generate_session_cookies": "1",
	"generate_analytics_claim": "1",
	"generate_machine_id": "1",
	"tier": "regular",
	"device": "Infinix X682B", # --> From Parsing User Agent
	"os_ver": "4.0.0", # --> From Parsing User Agent
	"app_id": "350685531728", # --> From App ID
	"app_ver": "348.719.618.179", # --> From Parsing User Agent
	"meta_inf_fbmeta": "NO_FILE", # --> Optional Value
	"currently_logged_in_userid" : "0",
	"fb_api_req_friendly_name": "authenticate",
	"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
	"fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
	"fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
	"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
	"api_key": "882a8490361da98702bf97a021ddc14d",
	"sig":"62f8ce9f74b12f84c123cc23437a4a32"} # --> Use App ID|Token/Sig
	
	###----------[ Many Other Data With Different Functions ]---------- ###
	#"method": "auth.login", # --> Under Certain Conditions (read the request description above)
	#"relative_url": "method/auth.login",
	#"omit_response_on_success": "false",
	#"logged_out_id": str(uuid.uuid()),
	#"interface": "wifi",
	#"reason", "unknown",
	#"headwind_version", "3",
	#"headwind_cursor", "{}",
	#"hash_id": str(uuid.uuid()),
	#"community_id": "",
	#"try_num": "1",
	#"cds_experiment_group": "-1",
	#"enroll_misauth": "false",
	#"jazoest", "",
	#"encrypted_msisdn": "",
	#"sim_country": "id",
	#"network_country": "id",
	#"should_query_for_animation": "true",
	#"flow": "CONTROLLER_INITIALIZATION",
	#"query_hash": "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40)),

###----------[ HEADERS FOR REQUESTS ]---------- ###
content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
headers = {
	"User-Agent": ugent,
	"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
	"X-FB-SIM-HNI": str(random.randint(20000, 40000)),
	"X-FB-Net-HNI": str(random.randint(20000, 40000)),
	"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
	"X-FB-Connection-Quality": "GOOD",
	"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
	"X-Fb-Net-Sid": "",
	"X-FB-HTTP-Engine": "Liger",
	"X-Tigon-Is-Retry": "False",
	"X-FB-Friendly-Name": "authenticate",
	"Content-Type": "application/x-www-form-urlencoded",
	"Content-Length": str(len(content_lenght))}
	
	###----------[ Many Other Headers With Different Functions ]---------- ###
	#"server_timestamps": "true",
	#"fb_api_caller_class": "graphservice",
	#"fb_api_analytics_tags": "["GraphServices"]",
	#"request_token": Token,
	#"Priority": "u=3, i",
	#"device_id": str(uuid.uuid4()),
	#"family_device_id": str(uuid.uuid4()),
	#"X-FB-Client-IP": "True",
	#"X-FB-Server-Cluster": "True",
	#"X-MSGR-Region": "FRC"

###----------[ REQUESTS POST ]---------- ###
post = ses.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers)

###----------[ GENERATE COOKIE FROM REQUESTS ]---------- ###
coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
######### --------------------------------------- #########
