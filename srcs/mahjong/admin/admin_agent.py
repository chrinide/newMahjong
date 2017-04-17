#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    代理模块
"""
from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH,BACK_PRE
from common.utilt import *
from datetime import datetime

@admin_app.get('/agent/list')
def getAgentList(redis,session):
    """
        代理列表
    """
    curTime = datetime.now()
    lang    = getLang()
    isList  = request.GET.get('list','').strip()
    createAgChildAccess = '1'
    aType = '0'

    if isList:
        pass
    else:
        info = {
                'title'                  :       '下线代理列表',
                'showPlus'               :       'true' if aType == '0' else 'false',
                'createAccess'           :       createAgChildAccess,
                'createUrl'              :       '/admin/ag/create',
                'listUrl'                :       BACK_PRE+'/agent/list?list=1',
                'STATIC_LAYUI_PATH'      :       STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'      :       STATIC_ADMIN_PATH 
        }
        return template('admin_agent_list',info=info,lang=lang)

@admin_app.get('/agent/info')
def getAgentInfo(redis,session):
    """
        查看代理消息
    """
    pass

@admin_app.get('/agent/create')
def getAgentCreate(redis,session):
    """
        创建代理
    """
    pass

@admin_app.get('/agent/modify')
def getAgentModify(redis,session):
    """
        代理修改
    """
    pass
