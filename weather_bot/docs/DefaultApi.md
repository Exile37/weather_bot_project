# swagger_client.DefaultApi

All URIs are relative to *https://api.weatherstack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete_location**](DefaultApi.md#autocomplete_location) | **GET** /autocomplete | Location Lookup/Autocomplete
[**get_current_weather**](DefaultApi.md#get_current_weather) | **GET** /current | Current Weather
[**get_historical_marine_weather**](DefaultApi.md#get_historical_marine_weather) | **GET** /past-marine | Historical Marine Weather
[**get_historical_weather**](DefaultApi.md#get_historical_weather) | **GET** /historical | Historical Weather
[**get_marine_weather**](DefaultApi.md#get_marine_weather) | **GET** /marine | Marine Weather
[**get_weather_forecast**](DefaultApi.md#get_weather_forecast) | **GET** /forecast | Weather Forecast

# **autocomplete_location**
> InlineResponse2005 autocomplete_location(access_key, query, param_callback=param_callback)

Location Lookup/Autocomplete

The Weatherstack API's Location Lookup/Autocomplete endpoint can be used to pinpoint one or more specific locations and their identifying response objects with the aim of later passing them to a weather data endpoint. In our example below, we are looking for London, United Kingdom. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: WeatherstackKey
configuration = swagger_client.Configuration()
configuration.api_key['access_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
access_key = NULL # object | Your Weatherstack API access key. Find it in your Weatherstack dashboard.
query = NULL # object | Free-text location identifier. Examples: `New York`, `London, UK`, `51.5074,-0.1278`, `fetch:ip` (auto-detect by requester's IP). For bulk queries pass semicolon-separated locations (Professional and higher plans). 
param_callback = NULL # object | JSONP callback function name. When present, the API response is wrapped for JSONP. (optional)

try:
    # Location Lookup/Autocomplete
    api_response = api_instance.autocomplete_location(access_key, query, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->autocomplete_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | [**object**](.md)| Your Weatherstack API access key. Find it in your Weatherstack dashboard. | 
 **query** | [**object**](.md)| Free-text location identifier. Examples: &#x60;New York&#x60;, &#x60;London, UK&#x60;, &#x60;51.5074,-0.1278&#x60;, &#x60;fetch:ip&#x60; (auto-detect by requester&#x27;s IP). For bulk queries pass semicolon-separated locations (Professional and higher plans).  | 
 **param_callback** | [**object**](.md)| JSONP callback function name. When present, the API response is wrapped for JSONP. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[WeatherstackKey](../README.md#WeatherstackKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_weather**
> InlineResponse200 get_current_weather(access_key, query, units=units, language=language, param_callback=param_callback)

Current Weather

To query the Weatherstack API for real-time weather data in a location of your choice, simply attach your preferred location to the API's `current` endpoint as seen in the example request below. Depending on your subscription, you can also make a bulk location request by passing multiple semicolon-separated locations to the API URL. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: WeatherstackKey
configuration = swagger_client.Configuration()
configuration.api_key['access_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
access_key = NULL # object | Your Weatherstack API access key. Find it in your Weatherstack dashboard.
query = NULL # object | Free-text location identifier. Examples: `New York`, `London, UK`, `51.5074,-0.1278`, `fetch:ip` (auto-detect by requester's IP). For bulk queries pass semicolon-separated locations (Professional and higher plans). 
units = NULL # object | Units system for returned values. `m` = Metric (default), `s` = Scientific, `f` = Fahrenheit.  (optional)
language = NULL # object | Optional ISO 2-letter language code to localize text fields (where supported). (optional)
param_callback = NULL # object | JSONP callback function name. When present, the API response is wrapped for JSONP. (optional)

try:
    # Current Weather
    api_response = api_instance.get_current_weather(access_key, query, units=units, language=language, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_current_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | [**object**](.md)| Your Weatherstack API access key. Find it in your Weatherstack dashboard. | 
 **query** | [**object**](.md)| Free-text location identifier. Examples: &#x60;New York&#x60;, &#x60;London, UK&#x60;, &#x60;51.5074,-0.1278&#x60;, &#x60;fetch:ip&#x60; (auto-detect by requester&#x27;s IP). For bulk queries pass semicolon-separated locations (Professional and higher plans).  | 
 **units** | [**object**](.md)| Units system for returned values. &#x60;m&#x60; &#x3D; Metric (default), &#x60;s&#x60; &#x3D; Scientific, &#x60;f&#x60; &#x3D; Fahrenheit.  | [optional] 
 **language** | [**object**](.md)| Optional ISO 2-letter language code to localize text fields (where supported). | [optional] 
 **param_callback** | [**object**](.md)| JSONP callback function name. When present, the API response is wrapped for JSONP. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[WeatherstackKey](../README.md#WeatherstackKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_marine_weather**
> InlineResponse2004 get_historical_marine_weather(access_key, latitude, longitude, historical_date_start, historical_date_end=historical_date_end, tide=tide, hourly=hourly, interval=interval, units=units, language=language, param_callback=param_callback)

Historical Marine Weather

The Historical Marine Weather API have marine data since 1st Jan, 2015 for a given `latitude` and `longitude`, as well as tide data. This endpoint will return weather elements such as temperature, precipitation (rainfall), weather description, weather icon, wind speed, Tide data, significant wave height, swell height, swell direction and swell period.      **Note:** *Each day and location included in your request counts toward your monthly API request limit. The historical marine time series supports a maximum time frame of 35 days.* 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: WeatherstackKey
configuration = swagger_client.Configuration()
configuration.api_key['access_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
access_key = NULL # object | Your Weatherstack API access key. Find it in your Weatherstack dashboard.
latitude = NULL # object | Latitude coordinate (decimal degrees) for marine endpoints.
longitude = NULL # object | Longitude coordinate (decimal degrees) for marine endpoints.
historical_date_start = NULL # object | Start date for a historical time-series (required for time-series requests).
historical_date_end = NULL # object | End date for a historical time-series request (maximum timeframe: 60 days). (optional)
tide = NULL # object | Set `tide=yes` to include tidal information (where available). Defaults to `no`. (optional)
hourly = NULL # object | Set to `1` to include hourly breakdown, or `0` (default) to omit hourly data. (optional)
interval = NULL # object | When `hourly=1`, defines the spacing of hourly entries: 1 (hourly), 3 (default), 6, 12, or 24 (day average).  (optional)
units = NULL # object | Units system for returned values. `m` = Metric (default), `s` = Scientific, `f` = Fahrenheit.  (optional)
language = NULL # object | Optional ISO 2-letter language code to localize text fields (where supported). (optional)
param_callback = NULL # object | JSONP callback function name. When present, the API response is wrapped for JSONP. (optional)

try:
    # Historical Marine Weather
    api_response = api_instance.get_historical_marine_weather(access_key, latitude, longitude, historical_date_start, historical_date_end=historical_date_end, tide=tide, hourly=hourly, interval=interval, units=units, language=language, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_historical_marine_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | [**object**](.md)| Your Weatherstack API access key. Find it in your Weatherstack dashboard. | 
 **latitude** | [**object**](.md)| Latitude coordinate (decimal degrees) for marine endpoints. | 
 **longitude** | [**object**](.md)| Longitude coordinate (decimal degrees) for marine endpoints. | 
 **historical_date_start** | [**object**](.md)| Start date for a historical time-series (required for time-series requests). | 
 **historical_date_end** | [**object**](.md)| End date for a historical time-series request (maximum timeframe: 60 days). | [optional] 
 **tide** | [**object**](.md)| Set &#x60;tide&#x3D;yes&#x60; to include tidal information (where available). Defaults to &#x60;no&#x60;. | [optional] 
 **hourly** | [**object**](.md)| Set to &#x60;1&#x60; to include hourly breakdown, or &#x60;0&#x60; (default) to omit hourly data. | [optional] 
 **interval** | [**object**](.md)| When &#x60;hourly&#x3D;1&#x60;, defines the spacing of hourly entries: 1 (hourly), 3 (default), 6, 12, or 24 (day average).  | [optional] 
 **units** | [**object**](.md)| Units system for returned values. &#x60;m&#x60; &#x3D; Metric (default), &#x60;s&#x60; &#x3D; Scientific, &#x60;f&#x60; &#x3D; Fahrenheit.  | [optional] 
 **language** | [**object**](.md)| Optional ISO 2-letter language code to localize text fields (where supported). | [optional] 
 **param_callback** | [**object**](.md)| JSONP callback function name. When present, the API response is wrapped for JSONP. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[WeatherstackKey](../README.md#WeatherstackKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_historical_weather**
> InlineResponse2002 get_historical_weather(access_key, query, historical_date, historical_date_start=historical_date_start, historical_date_end=historical_date_end, hourly=hourly, interval=interval, units=units, language=language, param_callback=param_callback)

Historical Weather

To look up historical weather data all the way back to 2015, simply pass one date of your choice (later than July 2008) or multiple semicolon-separated dates to the Weatherstack API's Historical Weather endpoint using the  `historical_date` parameter. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: WeatherstackKey
configuration = swagger_client.Configuration()
configuration.api_key['access_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
access_key = NULL # object | Your Weatherstack API access key. Find it in your Weatherstack dashboard.
query = NULL # object | Free-text location identifier. Examples: `New York`, `London, UK`, `51.5074,-0.1278`, `fetch:ip` (auto-detect by requester's IP). For bulk queries pass semicolon-separated locations (Professional and higher plans). 
historical_date = NULL # object | Single historical date (YYYY-MM-DD) or semicolon-separated list of dates. Used to request specific historical days (availability depends on subscription and archives). 
historical_date_start = NULL # object | Start date for a historical time-series (required for time-series requests). (optional)
historical_date_end = NULL # object | End date for a historical time-series request (maximum timeframe: 60 days). (optional)
hourly = NULL # object | Set to `1` to include hourly breakdown, or `0` (default) to omit hourly data. (optional)
interval = NULL # object | When `hourly=1`, defines the spacing of hourly entries: 1 (hourly), 3 (default), 6, 12, or 24 (day average).  (optional)
units = NULL # object | Units system for returned values. `m` = Metric (default), `s` = Scientific, `f` = Fahrenheit.  (optional)
language = NULL # object | Optional ISO 2-letter language code to localize text fields (where supported). (optional)
param_callback = NULL # object | JSONP callback function name. When present, the API response is wrapped for JSONP. (optional)

try:
    # Historical Weather
    api_response = api_instance.get_historical_weather(access_key, query, historical_date, historical_date_start=historical_date_start, historical_date_end=historical_date_end, hourly=hourly, interval=interval, units=units, language=language, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_historical_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | [**object**](.md)| Your Weatherstack API access key. Find it in your Weatherstack dashboard. | 
 **query** | [**object**](.md)| Free-text location identifier. Examples: &#x60;New York&#x60;, &#x60;London, UK&#x60;, &#x60;51.5074,-0.1278&#x60;, &#x60;fetch:ip&#x60; (auto-detect by requester&#x27;s IP). For bulk queries pass semicolon-separated locations (Professional and higher plans).  | 
 **historical_date** | [**object**](.md)| Single historical date (YYYY-MM-DD) or semicolon-separated list of dates. Used to request specific historical days (availability depends on subscription and archives).  | 
 **historical_date_start** | [**object**](.md)| Start date for a historical time-series (required for time-series requests). | [optional] 
 **historical_date_end** | [**object**](.md)| End date for a historical time-series request (maximum timeframe: 60 days). | [optional] 
 **hourly** | [**object**](.md)| Set to &#x60;1&#x60; to include hourly breakdown, or &#x60;0&#x60; (default) to omit hourly data. | [optional] 
 **interval** | [**object**](.md)| When &#x60;hourly&#x3D;1&#x60;, defines the spacing of hourly entries: 1 (hourly), 3 (default), 6, 12, or 24 (day average).  | [optional] 
 **units** | [**object**](.md)| Units system for returned values. &#x60;m&#x60; &#x3D; Metric (default), &#x60;s&#x60; &#x3D; Scientific, &#x60;f&#x60; &#x3D; Fahrenheit.  | [optional] 
 **language** | [**object**](.md)| Optional ISO 2-letter language code to localize text fields (where supported). | [optional] 
 **param_callback** | [**object**](.md)| JSONP callback function name. When present, the API response is wrapped for JSONP. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[WeatherstackKey](../README.md#WeatherstackKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marine_weather**
> InlineResponse2003 get_marine_weather(access_key, latitude, longitude, tide=tide, hourly=hourly, interval=interval, units=units, language=language, param_callback=param_callback)

Marine Weather

The Marine Weather API endpoint will allow to access today's live marine/sailing weather forecast for a given `longitude` and `latitude` , as well as up to 7 days of forecast. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: WeatherstackKey
configuration = swagger_client.Configuration()
configuration.api_key['access_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
access_key = NULL # object | Your Weatherstack API access key. Find it in your Weatherstack dashboard.
latitude = NULL # object | Latitude coordinate (decimal degrees) for marine endpoints.
longitude = NULL # object | Longitude coordinate (decimal degrees) for marine endpoints.
tide = NULL # object | Set `tide=yes` to include tidal information (where available). Defaults to `no`. (optional)
hourly = NULL # object | Set to `1` to include hourly breakdown, or `0` (default) to omit hourly data. (optional)
interval = NULL # object | When `hourly=1`, defines the spacing of hourly entries: 1 (hourly), 3 (default), 6, 12, or 24 (day average).  (optional)
units = NULL # object | Units system for returned values. `m` = Metric (default), `s` = Scientific, `f` = Fahrenheit.  (optional)
language = NULL # object | Optional ISO 2-letter language code to localize text fields (where supported). (optional)
param_callback = NULL # object | JSONP callback function name. When present, the API response is wrapped for JSONP. (optional)

try:
    # Marine Weather
    api_response = api_instance.get_marine_weather(access_key, latitude, longitude, tide=tide, hourly=hourly, interval=interval, units=units, language=language, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_marine_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | [**object**](.md)| Your Weatherstack API access key. Find it in your Weatherstack dashboard. | 
 **latitude** | [**object**](.md)| Latitude coordinate (decimal degrees) for marine endpoints. | 
 **longitude** | [**object**](.md)| Longitude coordinate (decimal degrees) for marine endpoints. | 
 **tide** | [**object**](.md)| Set &#x60;tide&#x3D;yes&#x60; to include tidal information (where available). Defaults to &#x60;no&#x60;. | [optional] 
 **hourly** | [**object**](.md)| Set to &#x60;1&#x60; to include hourly breakdown, or &#x60;0&#x60; (default) to omit hourly data. | [optional] 
 **interval** | [**object**](.md)| When &#x60;hourly&#x3D;1&#x60;, defines the spacing of hourly entries: 1 (hourly), 3 (default), 6, 12, or 24 (day average).  | [optional] 
 **units** | [**object**](.md)| Units system for returned values. &#x60;m&#x60; &#x3D; Metric (default), &#x60;s&#x60; &#x3D; Scientific, &#x60;f&#x60; &#x3D; Fahrenheit.  | [optional] 
 **language** | [**object**](.md)| Optional ISO 2-letter language code to localize text fields (where supported). | [optional] 
 **param_callback** | [**object**](.md)| JSONP callback function name. When present, the API response is wrapped for JSONP. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[WeatherstackKey](../README.md#WeatherstackKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weather_forecast**
> InlineResponse2001 get_weather_forecast(access_key, query, forecast_days=forecast_days, hourly=hourly, interval=interval, units=units, language=language, param_callback=param_callback)

Weather Forecast

The Weatherstack API is capable of returning weather forecast data for up to 14 days into the future. To get weather forecasts, simply use the API's Weather Forecast endpoint and define your preferred number of forecast days using the `forecast_days` parameter. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: WeatherstackKey
configuration = swagger_client.Configuration()
configuration.api_key['access_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
access_key = NULL # object | Your Weatherstack API access key. Find it in your Weatherstack dashboard.
query = NULL # object | Free-text location identifier. Examples: `New York`, `London, UK`, `51.5074,-0.1278`, `fetch:ip` (auto-detect by requester's IP). For bulk queries pass semicolon-separated locations (Professional and higher plans). 
forecast_days = NULL # object | Number of days of forecast to return (depends on subscription; up to 14 days). (optional)
hourly = NULL # object | Set to `1` to include hourly breakdown, or `0` (default) to omit hourly data. (optional)
interval = NULL # object | When `hourly=1`, defines the spacing of hourly entries: 1 (hourly), 3 (default), 6, 12, or 24 (day average).  (optional)
units = NULL # object | Units system for returned values. `m` = Metric (default), `s` = Scientific, `f` = Fahrenheit.  (optional)
language = NULL # object | Optional ISO 2-letter language code to localize text fields (where supported). (optional)
param_callback = NULL # object | JSONP callback function name. When present, the API response is wrapped for JSONP. (optional)

try:
    # Weather Forecast
    api_response = api_instance.get_weather_forecast(access_key, query, forecast_days=forecast_days, hourly=hourly, interval=interval, units=units, language=language, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_weather_forecast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | [**object**](.md)| Your Weatherstack API access key. Find it in your Weatherstack dashboard. | 
 **query** | [**object**](.md)| Free-text location identifier. Examples: &#x60;New York&#x60;, &#x60;London, UK&#x60;, &#x60;51.5074,-0.1278&#x60;, &#x60;fetch:ip&#x60; (auto-detect by requester&#x27;s IP). For bulk queries pass semicolon-separated locations (Professional and higher plans).  | 
 **forecast_days** | [**object**](.md)| Number of days of forecast to return (depends on subscription; up to 14 days). | [optional] 
 **hourly** | [**object**](.md)| Set to &#x60;1&#x60; to include hourly breakdown, or &#x60;0&#x60; (default) to omit hourly data. | [optional] 
 **interval** | [**object**](.md)| When &#x60;hourly&#x3D;1&#x60;, defines the spacing of hourly entries: 1 (hourly), 3 (default), 6, 12, or 24 (day average).  | [optional] 
 **units** | [**object**](.md)| Units system for returned values. &#x60;m&#x60; &#x3D; Metric (default), &#x60;s&#x60; &#x3D; Scientific, &#x60;f&#x60; &#x3D; Fahrenheit.  | [optional] 
 **language** | [**object**](.md)| Optional ISO 2-letter language code to localize text fields (where supported). | [optional] 
 **param_callback** | [**object**](.md)| JSONP callback function name. When present, the API response is wrapped for JSONP. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[WeatherstackKey](../README.md#WeatherstackKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

