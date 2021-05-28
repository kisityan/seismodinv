#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#该脚本用于在2d速度模型中添加矩形异常体，被generate_velocity_models_anomalies.py调用#


import numpy as np
import matplotlib.pyplot as plt


def add_anomalies(c,velocity,i,vm_s):


    
    ####################################自由度为0
    if c.freedom == 0:
        m = vm_s[0]#控制背景速度模型是否固定
        layer_thickness=m[0].copy()
        layer_thickness[0]+=1
        layer_thickness[len(m[0])-1]=layer_thickness[len(m[0])-1]-1
        anomal_layer_number = 1#控制异常体生成层
        anomal_layer_start_index=0
        for xx in np.arange(0,anomal_layer_number):
            anomal_layer_start_index += layer_thickness[xx]
        anomal_thickness = int(0.5 * layer_thickness[anomal_layer_number])#控制异常体宽度和厚度
        anomal_width = int(0.5 * c.vm_ns["x"])
        if (layer_thickness[anomal_layer_number] - anomal_thickness)%2 != 0:
                anomal_thickness += 1   
        if anomal_width % 2 != 0:
                 anomal_width += 1
        anomal_i = int((c.vm_ns["x"] - anomal_width)/2 + 0 )#控制异常体的水平和垂向位置
        anomal_j = int((layer_thickness[anomal_layer_number] - anomal_thickness)/2 + anomal_layer_start_index )
        percent = np.random.uniform(c.anomal_dv_percent[0],c.anomal_dv_percent[1])
        if np.random.random() > 0.5: 
                percent *= -1
        for iii in np.arange(anomal_i,anomal_i+anomal_width+1):
            for jjj in np.arange(anomal_j,anomal_j+anomal_thickness+1):
                velocity[iii,jjj]=m[1][anomal_layer_number]*(1+percent)

    ##############################################自由度为1
    if c.freedom == 1:
        m = vm_s[0]
        layer_thickness=m[0].copy()
        layer_thickness[0]+=1
        layer_thickness[len(m[0])-1]=layer_thickness[len(m[0])-1]-1
        anomal_layer_number = 1
        anomal_layer_start_index=0
        for xx in np.arange(0,anomal_layer_number):
            anomal_layer_start_index += layer_thickness[xx]
        anomal_thickness = np.random.randint(c.anomal_thickness_percent[0]*layer_thickness[anomal_layer_number],c.anomal_thickness_percent[1]*layer_thickness[anomal_layer_number])
        anomal_width = np.random.randint(c.anomal_width_percent[0]*c.vm_ns["x"],c.anomal_width_percent[1]*c.vm_ns["x"])
        if (layer_thickness[anomal_layer_number] - anomal_thickness)%2 != 0:
                anomal_thickness += 1   
        if anomal_width % 2 != 0:
                 anomal_width += 1
        anomal_i = int((c.vm_ns["x"] - anomal_width)/2 + 0 )
        anomal_j = int((layer_thickness[anomal_layer_number] - anomal_thickness)/2 + anomal_layer_start_index )
        percent = np.random.uniform(c.anomal_dv_percent[0],c.anomal_dv_percent[1])
        if np.random.random() > 0.5: 
                percent *= -1
        for iii in np.arange(anomal_i,anomal_i+anomal_width+1):
            for jjj in np.arange(anomal_j,anomal_j+anomal_thickness+1):
                velocity[iii,jjj]=m[1][anomal_layer_number]*(1+percent)
    ##############################################自由度为2
    if c.freedom == 2:
        m = vm_s[i]
        layer_thickness=m[0].copy()
        layer_thickness[0]+=1
        layer_thickness[len(m[0])-1]=layer_thickness[len(m[0])-1]-1
        anomal_layer_number = 1
        anomal_layer_start_index=0
        for xx in np.arange(0,anomal_layer_number):
            anomal_layer_start_index += layer_thickness[xx]
        anomal_thickness = np.random.randint(c.anomal_thickness_percent[0]*layer_thickness[anomal_layer_number],c.anomal_thickness_percent[1]*layer_thickness[anomal_layer_number])
        anomal_width = np.random.randint(c.anomal_width_percent[0]*c.vm_ns["x"],c.anomal_width_percent[1]*c.vm_ns["x"])
        if (layer_thickness[anomal_layer_number] - anomal_thickness)%2 != 0:
            anomal_thickness += 1      
        if anomal_width % 2 != 0:
            anomal_width += 1
        anomal_i = int((c.vm_ns["x"] - anomal_width)/2 + 0 )
        anomal_j = int((layer_thickness[anomal_layer_number] - anomal_thickness)/2 + anomal_layer_start_index )
        percent = np.random.uniform(c.anomal_dv_percent[0],c.anomal_dv_percent[1])
        if np.random.random() > 0.5: 
                percent *= -1
        for iii in np.arange(anomal_i,anomal_i+anomal_width+1):
            for jjj in np.arange(anomal_j,anomal_j+anomal_thickness+1):
                velocity[iii,jjj]=m[1][anomal_layer_number]*(1+percent)
    ##############################################自由度为3
    if c.freedom == 3:
        m = vm_s[i]
        layer_thickness=m[0].copy()
        layer_thickness[0]+=1
        layer_thickness[len(m[0])-1]=layer_thickness[len(m[0])-1]-1
        anomal_layer_number = 1
        anomal_layer_start_index=0
        for xx in np.arange(0,anomal_layer_number):
            anomal_layer_start_index += layer_thickness[xx]
        anomal_thickness = np.random.randint(c.anomal_thickness_percent[0]*layer_thickness[anomal_layer_number],c.anomal_thickness_percent[1]*layer_thickness[anomal_layer_number])
        anomal_width = np.random.randint(c.anomal_width_percent[0]*c.vm_ns["x"],c.anomal_width_percent[1]*c.vm_ns["x"])
        anomal_thickness = np.random.randint(c.anomal_thickness_percent[0]*layer_thickness[anomal_layer_number],c.anomal_thickness_percent[1]*layer_thickness[anomal_layer_number])
        anomal_width = np.random.randint(c.anomal_width_percent[0]*c.vm_ns["x"],c.anomal_width_percent[1]*c.vm_ns["x"])    
        anomal_up = int(anomal_layer_start_index + c.anomal_vertical_limit[0]*layer_thickness[anomal_layer_number])
        anomal_lower = int(anomal_layer_start_index + c.anomal_vertical_limit[1]*layer_thickness[anomal_layer_number])      
        anomal_left = int(0 + c.anomal_horizon_limit[0]*c.vm_ns["x"])
        anomal_right = int(0 + c.anomal_horizon_limit[1]*c.vm_ns["x"])
        anomal_j = np.random.randint(anomal_up,anomal_lower)
        anomal_i = np.random.randint(anomal_left,anomal_right)
        percent = np.random.uniform(c.anomal_dv_percent[0],c.anomal_dv_percent[1])
        if np.random.random() > 0.5: 
                percent *= -1
        for iii in np.arange(anomal_i,anomal_i+anomal_width+1):
            for jjj in np.arange(anomal_j,anomal_j+anomal_thickness+1):
                velocity[iii,jjj]=m[1][anomal_layer_number]*(1+percent)
     ##############################################自由度为4 
    if c.freedom == 4:
        m = vm_s[i]
        layer_thickness=m[0].copy()
        layer_thickness[0]+=1
        layer_thickness[len(m[0])-1]=layer_thickness[len(m[0])-1]-1
        anomal_layer_number=np.random.randint(1,len(m[0])-1)
        anomal_layer_start_index=0
        for xx in np.arange(0,anomal_layer_number):
            anomal_layer_start_index += layer_thickness[xx]
        anomal_thickness = np.random.randint(c.anomal_thickness_percent[0]*layer_thickness[anomal_layer_number],c.anomal_thickness_percent[1]*layer_thickness[anomal_layer_number])
        anomal_width = np.random.randint(c.anomal_width_percent[0]*c.vm_ns["x"],c.anomal_width_percent[1]*c.vm_ns["x"])
        anomal_thickness = np.random.randint(c.anomal_thickness_percent[0]*layer_thickness[anomal_layer_number],c.anomal_thickness_percent[1]*layer_thickness[anomal_layer_number])
        anomal_width = np.random.randint(c.anomal_width_percent[0]*c.vm_ns["x"],c.anomal_width_percent[1]*c.vm_ns["x"])    
        anomal_up = int(anomal_layer_start_index + c.anomal_vertical_limit[0]*layer_thickness[anomal_layer_number])
        anomal_lower = int(anomal_layer_start_index + c.anomal_vertical_limit[1]*layer_thickness[anomal_layer_number])      
        anomal_left = int(0 + c.anomal_horizon_limit[0]*c.vm_ns["x"])
        anomal_right = int(0 + c.anomal_horizon_limit[1]*c.vm_ns["x"])
        anomal_j = np.random.randint(anomal_up,anomal_lower)
        anomal_i = np.random.randint(anomal_left,anomal_right)
        percent = np.random.uniform(c.anomal_dv_percent[0],c.anomal_dv_percent[1])
        if np.random.random() > 0.5: 
                percent *= -1
        for iii in np.arange(anomal_i,anomal_i+anomal_width+1):
            for jjj in np.arange(anomal_j,anomal_j+anomal_thickness+1):
                velocity[iii,jjj]=m[1][anomal_layer_number]*(1+percent)


    return velocity

