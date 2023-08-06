"""The AWS database Action. This will pull the AWS rds"""
from threemystic_cloud_data_client.cloud_providers.aws.client.actions.base_class.base import cloud_data_client_aws_client_action_base as base
import asyncio
from decimal import Decimal, ROUND_HALF_UP

class cloud_data_client_aws_client_action(base):
  def __init__(self, *args, **kwargs):
    super().__init__(
      data_action="budget",
      logger_name= "cloud_data_client_aws_client_action_budget",
      *args, **kwargs)
  
  async def _process_account_data_region(self, account, region, resource_groups, loop, *args, **kwargs):
    pass

  def __init_costdata_month(self, data_dt, *args, **kwargs):
    return {
      "currency": self.get_common().helper_type().string().set_case(self.get_cloud_data_client().get_default_currency(), case= "upper"),
      "month": data_dt.month,
      "year": data_dt.year,
      "totals":{
        "total": Decimal(0),
        "fiscal_total": Decimal(0),
        "forcast_total": Decimal(0),
        "fiscal_forcast_total": Decimal(0),
        "resource_group": {
          "total":{},
          "forcast_total":{},
          "origional_currency_total":{},
          "origional_currency_forcast_total":{},
        },
        "resource_type": {
          "total":{},
          "forcast_total":{},
          "origional_currency_total":{},
          "origional_currency_forcast_total":{},
        }
      },
      "days":{}
    }
  
  def __init_costdata_month_day(self, data_dt, currency, *args, **kwargs):
    return {
      "currency": self.get_common().helper_type().string().set_case(self.get_cloud_data_client().get_default_currency(), case= "upper"),
      "origional_currency": self.get_common().helper_type().string().set_case(string_value= currency, case= "upper"),
      "date": data_dt,
      "total": Decimal(0),
      "forcast_total": Decimal(0),
      "origional_currency_total": Decimal(0),
      "origional_currency_forcast_total": Decimal(0),
      "resource_group": {
        "total":{},
        "forcast_total":{},
        "origional_currency_total":{},
        "origional_currency_forcast_total":{},
      },
      "resource_type": {
        "total":{},
        "forcast_total":{},
        "origional_currency_total":{},
        "origional_currency_forcast_total":{},
      }
    }
  
  async def __process_get_cost_data_process_forcast(self, year_data, client, account, start_date, end_date, fiscal_start, fiscal_end, forecast_metrics, *args, **kwargs):
    
    results_by_time_forcast = self.get_cloud_client().general_boto_call_array(
      boto_call=lambda: client.get_cost_and_usage(
        TimePeriod={
          'Start': start_date.strftime("%Y-%m-%d"),
          'End': end_date.strftime("%Y-%m-%d"),
        },
        Granularity='DAILY',
        Metrics=forecast_metrics,
        Filter={
          "Dimensions":{
            "Key":"LINKED_ACCOUNT",
            "Values":[self.get_cloud_client().get_account_id(account= account)]
          }
        },
      ),
      boto_params= None,
      boto_nextkey = None,
      boto_key= None
    )
    
    total_key = "forcast_total"
    currency = results_by_time_forcast["Total"]["Unit"]
    
    for forecast_metric in forecast_metrics:
      year_data[forecast_metric] = {}
      for cost_data in results_by_time_forcast["ForecastResultsByTime"]:
        data_dt = self.get_common().helper_type().datetime().datetime_from_string(dt_string= str(cost_data["TimePeriod"]["Start"]), dt_format= "%Y-%m-%d")
        by_month_key = self.get_common().helper_type().datetime().datetime_as_string(dt_format= "%Y%m", dt= data_dt)

        day_key = self.get_common().helper_type().datetime().datetime_as_string(dt_format= "%Y%m%d", dt= data_dt)
        if year_data.get(by_month_key) is None:
          year_data[forecast_metric][by_month_key] = self.__init_costdata_month(data_dt= data_dt)
        
        if year_data[forecast_metric][by_month_key]["days"].get(day_key) is None:
          year_data[forecast_metric][by_month_key]["days"][day_key] = self.__init_costdata_month_day(data_dt= data_dt, currency= currency)
        
        raw_row_data_cost = (cost_data["MeanValue"])
        row_data_cost = (cost_data["MeanValue"])
        
        if year_data[forecast_metric][by_month_key]["days"][day_key]["currency"] != year_data[forecast_metric][by_month_key]["days"][day_key]["origional_currency"]:
          row_data_cost = self.get_common().helper_currency().convert(
            ammount= row_data_cost,
            currency_from= currency,
            currency_to= year_data[forecast_metric][by_month_key]["days"][day_key]["currency"],
            conversion_date= self.get_common().helper_type().datetime().yesterday(dt=self.get_common().helper_type().datetime().datetime_from_string(
              dt_string= self.get_common().helper_type().datetime().datetime_as_string(
                dt= data_dt,
                dt_format= "%Y%m01"
              ),
              dt_format= "%Y%m%d"
            )).date()
          )

        year_data[forecast_metric][by_month_key]["days"][day_key][f'origional_currency_{total_key}'] += Decimal(raw_row_data_cost)
        year_data[forecast_metric][by_month_key]["days"][day_key][f'{total_key}'] += Decimal(row_data_cost)
        year_data[forecast_metric][by_month_key]["totals"][f'{total_key}'] += Decimal(row_data_cost)
        if data_dt >= fiscal_start and data_dt <= fiscal_end:
          year_data[forecast_metric][by_month_key]["totals"][f'fiscal_{total_key}'] += Decimal(row_data_cost)


  async def __process_get_cost_data_process_year_data(self, year_data, client, account, start_date, end_date, fiscal_start, fiscal_end, forecast_metrics, *args, **kwargs):

    results_by_time = self.get_cloud_client().general_boto_call_array(
      boto_call=lambda: client.get_cost_and_usage(
        TimePeriod={
          'Start': start_date.strftime("%Y-%m-%d"),
          'End': end_date.strftime("%Y-%m-%d"),
        },
        Granularity='DAILY',
        Metrics=forecast_metrics,
        Filter={
          "Dimensions":{
            "Key":"LINKED_ACCOUNT",
            "Values":[self.get_cloud_client().get_account_id(account= account)]
          }
        },
        GroupBy= [
          {
            "Type": "DIMENSION",
            "Key": "SERVICE"
          }
        ]
      ),
      boto_params= None,
      boto_nextkey = "NextPageToken",
      boto_nextkey_param = "NextPageToken",
      boto_key="ResultsByTime"
    )
    
    total_key = "total"
    for forecast_metric in forecast_metrics:
      year_data[forecast_metric] = {}
      for cost_data in results_by_time:
        data_dt = self.get_common().helper_type().datetime().datetime_from_string(dt_string= str(cost_data["TimePeriod"]["Start"]), dt_format= "%Y-%m-%d")
        by_month_key = self.get_common().helper_type().datetime().datetime_as_string(dt_format= "%Y%m", dt= data_dt)

        day_key = self.get_common().helper_type().datetime().datetime_as_string(dt_format= "%Y%m%d", dt= data_dt)
        if year_data[forecast_metric].get(by_month_key) is None:
          year_data[forecast_metric][by_month_key] = self.__init_costdata_month(data_dt= data_dt)
        
        if year_data[forecast_metric][by_month_key]["days"].get(day_key) is None:
          year_data[forecast_metric][by_month_key]["days"][day_key] = cost_data["Total"]
          return 
          year_data[forecast_metric][by_month_key]["days"][day_key] = self.__init_costdata_month_day(data_dt= data_dt, currency= cost_data["Total"][forecast_metric]["Unit"])
        
        raw_row_data_cost = (cost_data["Total"][forecast_metric]["Amount"])
        row_data_cost = (cost_data["Total"][forecast_metric]["Amount"])
        
        if year_data[forecast_metric][by_month_key]["days"][day_key]["currency"] != year_data[forecast_metric][by_month_key]["days"][day_key]["origional_currency"]:
          row_data_cost = self.get_common().helper_currency().convert(
            ammount= row_data_cost,
            currency_from= year_data[forecast_metric][by_month_key]["days"][day_key]["origional_currency"],
            currency_to= year_data[forecast_metric][by_month_key]["days"][day_key]["currency"],
            conversion_date= self.get_common().helper_type().datetime().yesterday(dt=self.get_common().helper_type().datetime().datetime_from_string(
              dt_string= self.get_common().helper_type().datetime().datetime_as_string(
                dt= data_dt,
                dt_format= "%Y%m01"
              ),
              dt_format= "%Y%m%d"
            )).date()
          )

        year_data[forecast_metric][by_month_key]["days"][day_key][f'origional_currency_{total_key}'] += Decimal(raw_row_data_cost)
        year_data[forecast_metric][by_month_key]["days"][day_key][f'{total_key}'] += Decimal(row_data_cost)
        year_data[forecast_metric][by_month_key]["totals"][f'{total_key}'] += Decimal(row_data_cost)
        if data_dt >= fiscal_start and data_dt <= fiscal_end:
          year_data[forecast_metric][by_month_key]["totals"][f'fiscal_{total_key}'] += Decimal(row_data_cost)

        for cost_data_group in cost_data["Groups"]:
          raw_row_data_cost_group = cost_data_group["Metrics"][forecast_metric]["Amount"]
          row_data_cost_group = raw_row_data_cost_group
          
          if year_data[forecast_metric][by_month_key]["days"][day_key]["currency"] != cost_data_group["Metrics"][forecast_metric]["Unit"]:
            row_data_cost_group = self.get_common().helper_currency().convert(
              ammount= row_data_cost_group,
              currency_from= cost_data_group["Metrics"][forecast_metric]["Unit"],
              currency_to= year_data[forecast_metric][by_month_key]["days"][day_key]["currency"],
              conversion_date= self.get_common().helper_type().datetime().yesterday(dt=self.get_common().helper_type().datetime().datetime_from_string(
                dt_string= self.get_common().helper_type().datetime().datetime_as_string(
                  dt= data_dt,
                  dt_format= "%Y%m01"
                ),
                dt_format= "%Y%m%d"
              )).date()
            )
          for cost_data_group_key in cost_data_group["Keys"]:
            if (year_data[forecast_metric][by_month_key]["days"][day_key]["resource_type"][f'{total_key}'].get(cost_data_group_key) is None or
                year_data[forecast_metric][by_month_key]["days"][day_key]["resource_type"][f'origional_currency_{total_key}'].get(cost_data_group_key) is None):
              year_data[forecast_metric][by_month_key]["days"][day_key]["resource_type"][f'origional_currency_{total_key}'][cost_data_group_key] = Decimal(0)
              year_data[forecast_metric][by_month_key]["days"][day_key]["resource_type"][f'{total_key}'][cost_data_group_key] = Decimal(0)
            
            if (year_data[forecast_metric][by_month_key]["totals"]["resource_type"][f'{total_key}'].get(cost_data_group_key) is None or
                year_data[forecast_metric][by_month_key]["totals"]["resource_type"][f'origional_currency_{total_key}'].get(cost_data_group_key) is None):
              year_data[forecast_metric][by_month_key]["totals"]["resource_type"][f'origional_currency_{total_key}'][cost_data_group_key] = Decimal(0)
              year_data[forecast_metric][by_month_key]["totals"]["resource_type"][f'{total_key}'][cost_data_group_key] = Decimal(0)

            year_data[forecast_metric][by_month_key]["days"][day_key]["resource_type"][f'origional_currency_{total_key}'][cost_data_group_key] += Decimal(raw_row_data_cost_group)
            year_data[forecast_metric][by_month_key]["days"][day_key]["resource_type"][f'{total_key}'][cost_data_group_key] += Decimal(row_data_cost_group)
            year_data[forecast_metric][by_month_key]["totals"]["resource_type"][f'origional_currency_{total_key}'][cost_data_group_key] += Decimal(raw_row_data_cost_group)
            year_data[forecast_metric][by_month_key]["totals"]["resource_type"][f'{total_key}'][cost_data_group_key] += Decimal(row_data_cost_group)


  async def __process_get_cost_data(self, account, client, fiscal_year_start, loop, *args, **kwargs):
    fiscal_year_start_date = self.get_common().helper_type().datetime().datetime_from_string(
      dt_string= f"{self.get_data_start().year}/{fiscal_year_start}",
      dt_format= "%Y/%m/%d"
    )
    
    if fiscal_year_start_date > self.get_data_start():
      fiscal_year_start_date = fiscal_year_start_date + self.get_common().helper_type().datetime().time_delta(years= -1)

    fiscal_year_end = self.get_common().helper_type().datetime().yesterday(dt= (fiscal_year_start_date
                 + self.get_common().helper_type().datetime().time_delta(years= 1, dt= fiscal_year_start_date)))
    

    start_date = (fiscal_year_start_date
                 + self.get_common().helper_type().datetime().time_delta(months= -1, dt= fiscal_year_start_date))
    
    forecast_end = (fiscal_year_end
                 + self.get_common().helper_type().datetime().time_delta(months= 3, dt= fiscal_year_end))
    

    year_data = {}
    forcast_metric = "NetUnblendedCost"
    await self.__process_get_cost_data_process_year_data(
      year_data= year_data,
      client= client,
      account= account,
      start_date= start_date,
      end_date= self.get_data_start() if forecast_end > self.get_data_start() else forecast_end,
      fiscal_start= fiscal_year_start_date, 
      fiscal_end= fiscal_year_end,
      forecast_metrics = [forcast_metric]
    )
    return year_data

    await self.__process_get_cost_data_process_forcast(
      year_data= year_data,
      client= client,
      account= account,
      start_date= start_date,
      end_date= self.get_data_start() if forecast_end > self.get_data_start() else forecast_end,
      fiscal_start= fiscal_year_start_date, 
      fiscal_end= fiscal_year_end,
      forecast_metrics = [forcast_metric]
    )

    month_key = self.get_common().helper_type().datetime().datetime_as_string(
      dt= self.get_data_start(),
      dt_format= "%Y%m"
    )
    last_month_key = self.get_common().helper_type().datetime().datetime_as_string(
      dt= (self.get_data_start() - self.get_common().helper_type().datetime().time_delta(days= (self.get_data_start().day + 1))),
      dt_format= "%Y%m"
    )
    
    return_data = {
      "year_to_date": Decimal(0),  
      "year_forecast": Decimal(0),
      "fiscal_year_to_date": Decimal(0),  
      "fiscal_year_forecast": Decimal(0),
      "month_to_date": Decimal(0),  
      "month_forecast": Decimal(0),
      "last_seven_days": Decimal(0),
      "raw_last_14_days": {},
      "last_month": Decimal(0),
    }

    day_count = 0
    for i in range(0,14):     
      month_key_last14 = self.get_common().helper_type().datetime().datetime_as_string(
        dt= (self.get_data_start() - self.get_common().helper_type().datetime().time_delta(days= i)),
        dt_format= "%Y%m"
      )
      day_key = self.get_common().helper_type().datetime().datetime_as_string(
        dt= (self.get_data_start() - self.get_common().helper_type().datetime().time_delta(days= i)),
        dt_format= "%Y%m%d"
      )

      if year_data[forcast_metric][month_key_last14]["days"].get(day_key) is None:
        continue
      
      return_data["raw_last_14_days"][day_key] = year_data[forcast_metric][month_key_last14]["days"].get(day_key)

      if day_count >= 7:
        continue

      day_count += 1
      return_data["last_seven_days"] += year_data[forcast_metric][month_key_last14]["days"][day_key]["total"]
      
    for data in year_data[forcast_metric].values():
      return_data["fiscal_year_to_date"] += data["totals"].get("fiscal_total")
      return_data["fiscal_year_forecast"] += (data["totals"].get("fiscal_total") + data["totals"].get("fiscal_forcast_total"))
      if data["year"] == self.get_data_start().year:
        return_data["year_to_date"] += data["totals"].get("total")
        return_data["year_forecast"] += (data["totals"].get("total") + data["totals"].get("forcast_total"))

    
    if year_data[forcast_metric].get(month_key) is not None:
      return_data["month_to_date"] = year_data[forcast_metric][month_key]["totals"]["total"]
      return_data["month_forecast"] = year_data[forcast_metric][month_key]["totals"]["total"] + year_data[forcast_metric][month_key]["totals"]["forcast_total"]
    
    if year_data[forcast_metric].get(last_month_key) is not None:
      return_data["last_month"] = year_data[forcast_metric][last_month_key]["totals"]["total"]
  
    return return_data


  async def _process_account_data(self, account, loop, *args, **kwargs):
    if self.get_common().helper_type().string().is_null_or_whitespace(string_value= kwargs.get("fiscal_year_start")):
      kwargs["fiscal_year_start"] = self.get_cloud_data_client().get_default_fiscal_year_start()
    
    client = self.get_cloud_client().get_boto_client(client= 'ce',  account=account)
  
    return {
      "account": account,
      "data": [ self.get_common().helper_type().dictionary().merge_dictionary([
        {},
        await self.get_base_return_data(
          account= account,
          resource_id =  f'{self.get_cloud_client().get_account_prefix()}{self.get_cloud_client().get_account_id(account= account)}',
        ),
        await self.__process_get_cost_data(account= account, client= client, loop= loop, *args, **kwargs)
      ])]
    }

  
