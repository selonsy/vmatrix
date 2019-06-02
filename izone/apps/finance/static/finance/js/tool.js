//prototype
document.write("<script src='/Content/js/common/prototype.js'></script>");
//opentips
document.write("<script src='/Content/lib/selonsy/jquery.opentips.js'></script>");

var tool = {};
var _tool = function () {

    var tool = {};

    //+----------------------------------------------------------------------  
    //| 功能：js数组去重
    //| 说明：
    //| 参数：
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2017-1-18 
    //+----------------------------------------------------------------------
    tool.uniQueue = function(array) {
        var arr = [];
        var m;
        while (array.length > 0) {
            m = array[0];
            arr.push(m);
            array = $.grep(array, function (n, i) {
                return n == m;
            }, true);
        }
        return arr;
    }

    //+----------------------------------------------------------------------  
    //| 功能：js数组去除指定元素
    //| 说明：
    //| 参数：
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2017-1-18 
    //+----------------------------------------------------------------------
    tool.removeByValue = function(arr, val) {
        for (var i = 0; i < arr.length; i++) {
            if (arr[i] == val) {
                arr.splice(i, 1);
                break;
            }
        }
        return arr;
    }

    //+----------------------------------------------------------------------  
    //| 功能：获取url里面的参数值
    //| 说明：
    //| 参数：
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2017-1-22 
    //+----------------------------------------------------------------------
    tool.getUrlParam = function(name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");     //构造一个含有目标参数的正则表达式对象
        var r = window.location.search.substr(1).match(reg);        //匹配目标参数
        //if (r != null) return unescape(r[2]); return null;          //返回参数值
        if (r != null) return decodeURI(r[2]); return null;          //返回参数值        
    }

    //+----------------------------------------------------------------------  
    //| 功能：获取url里面的参数对象
    //| 说明：
    //| 参数：
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2017-1-22 
    //+----------------------------------------------------------------------
    tool.getUrlParamObj = function() {
        var args = new Object();
        var query = window.location.search.substring(1);    //获取查询串   
        var pairs = query.split("&");                       //在逗号处断开   
        for (var i = 0; i < pairs.length; i++) {
            var pos = pairs[i].indexOf('=');                //查找name=value   
            if (pos == -1) continue;                        //如果没有找到就跳过   
            var argname = pairs[i].substring(0, pos);       //提取name   
            var value = pairs[i].substring(pos + 1);        //提取value   
            args[argname] = unescape(value);                //存为属性   
        }
        return args;
    }
    
    //+----------------------------------------------------------------------  
    //| 功能：检查Url是否合法
    //| 说明：
    //| 参数：
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2017-5-2 
    //+----------------------------------------------------------------------
    tool.checkUrl = function(value) {
        if (value != "") {
            var reg = new RegExp("^((https|http)://)(([0-9]{1,3}.){3}([0-9]{1,3})|([0-9a-z_!~*'()-]+.)*([0-9a-z][0-9a-z-]{0,61})?[0-9a-z].[a-z]{2,6})(:[0-9]{1,5})?((/?)|(/[0-9a-z_!~*'().;?:@&=+$,%#-]+)+/?)$");
            return reg.test(value);
        }
        return true;
    }

    //+----------------------------------------------------------------------  
    //| 功能：检查Email是否合法
    //| 说明：
    //| 参数：
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2017-5-2 
    //+----------------------------------------------------------------------    
    tool.checkEmail = function(value) {
        if (value != "") {
            var reg = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
            return reg.test(value)
        }
        return true;
    }    

    //+----------------------------------------------------------------------  
    //| 功能：检查Mobile是否合法
    //| 说明：
    //| 参数：
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2017-5-2 
    //+----------------------------------------------------------------------    
    tool.checkMobile = function(value) {
        if (value != "") {
            var reg = /^1[0-9]{10}$/;
            return reg.test(value)
        }
        return true;
    }

    //+----------------------------------------------------------------------  
    //| 功能：公用ajax调用函数(jQuery)
    //| 说明：支持是否异步
    //| 参数：url:页面地址,type:数据传递方式,data:要Post的数据,async:是否异步,asyncCall:回调函数;
    //| 返回值：如果是同步调用，则返回后台返回的值
    //| 创建人：沈金龙
    //| 创建时间：2016-1-29 17:26:42
    //+---------------------------------------------------------------------
    tool.myAjax = function(url, type, data, async, asyncCall) {
        var result;
        $.ajax({
            type: type,
            url: url,
            data: data,
            async: async,
            dataType: "text",
            //服务器返回的数据，描述状态的字符串
            success: function (data, textStatus) {
                //回调函数            
                if (asyncCall != undefined)
                    asyncCall(data, textStatus);
                if (async == false)
                    result = data;
            },
            //XMLHttpRequest对象、错误信息、捕获的错误对象
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                myAjaxError(XMLHttpRequest, textStatus, errorThrown);
            }
        });
        //回调函数调用在返回值之前
        return result;
    }

    //+----------------------------------------------------------------------  
    //| 功能：公用ajax调用函数(jQuery)
    //| 说明：
    //| 参数：
    //| url:页面地址,
    //| method:处理函数,需要有[WebMethod]的标识,
    //| data:参数列表,一定要是json格式的字符串,
    //| asyncCall:回调函数;
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2016-1-29 17:26:42
    //+---------------------------------------------------------------------
    tool.myAjaxWeb = function(url, method, data, asyncCall) {
        var xurl = url + "/" + method;
        var xdata = data == undefined ? "" : data;
        $.ajax({
            type: "Post", //WebMethod方法只接受post类型的请求           
            url: xurl,    //方法所在页面和方法名
            data: xdata,   //一定要是json格式的字符串
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (data, textStatus) {
                //返回的数据用data.d获取内容   
                if (asyncCall != undefined)
                    asyncCall(data.d, textStatus);
            },
            //XMLHttpRequest对象、错误信息、捕获的错误对象
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                myAjaxError(XMLHttpRequest, textStatus, errorThrown);
            }
        });
    }

    //+----------------------------------------------------------------------  
    //| 功能：原生异步调用函数
    //| 说明：
    //| 参数：
    //| url:页面地址,
    //| method:处理函数,需要有[WebMethod]的标识,
    //| data:参数列表,一定要是json格式的字符串,
    //| asyncCall:回调函数;
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2016-1-31 15:55:21
    //+---------------------------------------------------------------------
    tool.myAjaxXml = function() {
        //toodoo
    }

    //+----------------------------------------------------------------------  
    //| 功能：公用ajax错误处理函数(jQuery)
    //| 说明： 
    //| 参数：
    //| xmlHttpRequest：XMLHttpRequest对象
    //| textStatus：错误信息
    //| errorThrown：捕获的错误对象
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2016-1-29 17:26:42
    //+---------------------------------------------------------------------
    tool.myAjaxError = function(xmlHttpRequest, textStatus, errorThrown) {
        var msg = "status:" + xmlHttpRequest.status + "\n";
        msg += "Info:" + xmlHttpRequest.statusText + "\n";
        msg += "ResponseText:" + xmlHttpRequest.responseText + "\n";
        alert(msg);
    }

    //+----------------------------------------------------------------------  
    //| 功能：公用ajax表单提交函数.
    //| 说明：针对ajaxSubmit的二次封装. 
    //| 参数：
    //| xmlHttpRequest：XMLHttpRequest对象
    //| textStatus：错误信息
    //| errorThrown：捕获的错误对象
    //| 返回值：
    //| 创建人：沈金龙
    //| 创建时间：2016-1-29 17:26:42
    //+---------------------------------------------------------------------
    tool.myAjaxForm = function($form, filter, url, callback, istips) {
        var $submit = $form.find('.submit');
        var submitForm = function () {
            if (!filter()) return; //过滤条件
            $form.ajaxSubmit(function (rsp) {
                try {
                    var json = JSON.parse(jsp);
                    if (istips) alert(json.msg);
                    if (callback) {
                        callback(json);
                    }
                }
                catch (ex) {
                    //Todo:上传错误
                }
            });
        }
        $form.attr("action", url);
        $submit.click(submitForm);
    }

    return tool;
};
tool = _tool();