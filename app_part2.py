import langchain_core
from langchain_core.tools import tool
import app_part1
from app_part1 import fetch_product_details
import numpy as np, scipy
@tool
def calculation_reorder(conf_level: float, current_stock: float, daily_demand: int, lead_time_days: int, promotion_active: bool)->int:
    ''' This tool will return the reorder quantity for a product.
    It will calculate this based on the current stock, average daily demand, 
    procurement lead time, whether there is an active promotion going on, 
    and an expected confidence level that there will be no stockout.
    The details passed in the function are for a specific product so it is to be called once for each call'''
    reorder_point_wo_safety=daily_demand*lead_time_days
    demand_fluctuation=np.var(daily_demand)
    lead_time_fluctuation=np.var(lead_time_days)
    z_service_level=scipy.stats.norm.ppf(conf_level)
    safety_stock=z_service_level*np.sqrt((lead_time_days*demand_fluctuation)+(daily_demand*lead_time_fluctuation))
    if promotion_active=="Yes":
        safety_stock=safety_stock*1.5
    desired_qty=reorder_point_wo_safety+safety_stock
    return max(0, desired_qty-current_stock)