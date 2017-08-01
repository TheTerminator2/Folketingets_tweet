from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import json
import psycopg2

# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

#consumer key, consumer secret, access token, access secret.
ckey=ckey_
csecret=csecret_
atoken=atoken_
asecret=asecret_

#lookup arrays to convert user's timezone to a country
TimeZones = ['International Date Line West','Midway Island','American Samoa','Hawaii','Alaska','Pacific Time (US & Canada)','Tijuana','Mountain Time (US & Canada)','Arizona','Chihuahua','Mazatlan','Central Time (US & Canada)','Saskatchewan','Guadalajara','Mexico City','Monterrey','Central America','Eastern Time (US & Canada)','Indiana (East)','Bogota','Lima','Quito','Atlantic Time (Canada)','Caracas','La Paz','Santiago','Newfoundland','Brasilia','Buenos Aires','Montevideo','Georgetown','Greenland','Mid-Atlantic','Azores','Cape Verde Is.','Dublin','Edinburgh','Lisbon','London','Casablanca','Monrovia','UTC','Belgrade','Bratislava','Budapest','Ljubljana','Prague','Sarajevo','Skopje','Warsaw','Zagreb','Brussels','Copenhagen','Madrid','Paris','Amsterdam','Berlin','Bern','Rome','Stockholm','Vienna','West Central Africa','Bucharest','Cairo','Helsinki','Kyiv','Riga','Sofia','Tallinn','Vilnius','Athens','Istanbul','Minsk','Jerusalem','Harare','Pretoria','Kaliningrad','Moscow','St. Petersburg','Volgograd','Samara','Kuwait','Riyadh','Nairobi','Baghdad','Tehran','Abu Dhabi','Muscat','Baku','Tbilisi','Yerevan','Kabul','Ekaterinburg','Islamabad','Karachi','Tashkent','Chennai','Kolkata','Mumbai','New Delhi','Kathmandu','Astana','Dhaka','Sri Jayawardenepura','Almaty','Novosibirsk','Rangoon','Bangkok','Hanoi','Jakarta','Krasnoyarsk','Beijing','Chongqing','Hong Kong','Urumqi','Kuala Lumpur','Singapore','Taipei','Perth','Irkutsk','Ulaanbaatar','Seoul','Osaka','Sapporo','Tokyo','Yakutsk','Darwin','Adelaide','Canberra','Melbourne','Sydney','Brisbane','Hobart','Vladivostok','Guam','Port Moresby','Magadan','Srednekolymsk','Solomon Is.','New Caledonia','Fiji','Kamchatka','Marshall Is.','Auckland','Wellington',"Nuku'alofa",'Tokelau Is.','Chatham Is.','Samoa','Europe/London','America/New_York','EST']
Country = ['United States Minor Outlying Islands','United States Minor Outlying Islands','American Samoa','United States','United States','United States','Mexico','United States','United States','Mexico','Mexico','United States','Canada','Mexico','Mexico','Mexico','Guatemala','United States','United States','Colombia','Peru','Peru','Canada','Venezuela','Bolivia','Chile','Canada','Brazil','Argentina','Uruguay','Guyana','Greenland','South Georgia and the South Sandwich Islands','Portugal','Cape Verde','Ireland','United Kingdom','Portugal','United Kingdom','Morocco','Liberia','#N/A','Serbia','Slovakia','Hungary','Slovenia','Czech Republic','Bosnia and Herzegovina','Macedonia','Poland','Croatia','Belgium','Denmark','Spain','France','Netherlands','Germany','Germany','Italy','Sweden','Austria','Algeria','Romania','Egypt','Finland','Ukraine','Latvia','Bulgaria','Estonia','Lithuania','Greece','Turkey','Belarus','Israel','Zimbabwe','South Africa','Russia','Russia','Russia','Russia','Russia','Kuwait','Saudi Arabia','Kenya','Iraq','Iran','Oman','Oman','Azerbaijan','Georgia','Armenia','Afghanistan','Russia','Pakistan','Pakistan','Uzbekistan','India','India','India','India','Nepal','Bangladesh','Bangladesh','Sri Lanka','Kazakhstan','Russia','Myanmar','Thailand','Thailand','Indonesia','Russia','China','#N/A','Hong Kong','China','Malaysia','Singapore','Taiwan','Australia','Russia','Mongolia','South Korea','Japan','Japan','Japan','Russia','Australia','Australia','Australia','Australia','Australia','Australia','Australia','Russia','Guam','Papua New Guinea','Russia','Russia','Solomon Islands','New Caledonia','Fiji','Russia','Marshall Islands','New Zealand','New Zealand','Tonga','Tokelau','New Zealand','Samoa','United Kingdom','United States','United States']

#listner for twitter stream
class listener(StreamListener):
        def on_data(self, data):
            print(data)
            all_data  = json.loads(data)

            #insert data into database
            scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
            sqlite.save(data={"dat": all_data})

         return(True)

         except Exception as e:
             print(e)
             print (all_data)

         def on_error(self, status):
             print status


auth = OAuthHandler(ckey_, csecret_)
auth.set_access_token(atoken_, asecret_)


while True:
    try:
        twitterStream = Stream(auth, listener())
        twitterStream.filter(languages=["da"]) #insert keywords for Twitter search
        #twitterStream.sample() #random sample from twitter

    except:
        # Oh well, reconnect and keep going
        continue
