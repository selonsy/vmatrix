/*
 * 发送api请求
 */
function send(opt, successCall, failCall) {
    var dtd = $.Deferred();
    if (opt.data) {
        opt.data = $.extend(true, { 't': new Date().getTime() }, opt.data);
    } else {
        opt.data = { 't': new Date().getTime() };
    }
    opt = $.extend({}, {
        type: 'post',
        async: true,
        //dataType : "jsonp", //跨域使用
        //jsonp: 'callback',  //跨域使用,自定义回调函数名称
        beforeSend:function(xhr,settings){
            // 在Django中使用ajax post向后台传送数据时会出现403 Forbidden (CSRF token missing or incorrect.): 的报错。
            // django Forbidden (CSRF token missing or incorrect.): /finance/getlist
            // csrftoken:9gNQAICic3G1kaspSkKaf5yWj8NqIDZ0Ss6ZCwrqS9S5n4To5qcChn5OxXL7pQpm
            // 上面的在页面的cookie里面，django开启了csrf校验，在中间件里面 'django.middleware.csrf.CsrfViewMiddleware',
            xhr.setRequestHeader("X-CSRFToken","csrf_token");
        },
        success: function (jsp) {
            var json = jsp;
            if (jsp) {
                if (typeof (jsp) == "string") {
                    try {
                        json = JSON.parse(jsp);
                    } catch (ex) {
                        json = jsp;
                    }
                }
                if (json) {
                    if (json.code === 1) {
                        successCall && successCall();
                        dtd.resolve(json);
                    }
                    else {
                        failCall && failCall();
                        dtd.reject(json);
                    }
                }
            }
            else {
                dtd.reject();
            }
        },
        error: function (xhr, status) {
            failCall && failCall(xhr.responseText, status);
            dtd.reject(xhr.responseText);
        },
        complete: function (xhr, status) {
            if (status == 'timeout') {
                failCall && failCall({ 'Message': '请求超时' }, status);
                dtd.reject(xhr.responseText);
            }
        }
    }, opt);
    var ajax = $.ajax(opt);
    return dtd;
}

/*
 * 封装请求
 */
function build(url, defaultData, defaultOpt) {
    return function (data, success, fail, extendOpt) {
        var opt = defaultOpt || extendOpt ? $.extend({}, defaultOpt, extendOpt) : {};
        data = defaultData ? $.extend({}, defaultData, data) : data;
        opt.data = data;
        opt.url = url;
        return send(opt, success, fail);
    }
}

/**
 * 收集错误信息
 */
window.onerror = function (message, url, line) {
    var errorMsg = message + '\n';                          //错误信息
    errorMsg += 'FilePath:' + url + '\n';                   //文件位置
    errorMsg += 'URL:' + window.location.href + '\n';       //当前页面url
    errorMsg += 'Line:' + line + '\n';                      //错误行数
    errorMsg += 'Brower:' + navigator.userAgent.toString(); //浏览器信息

    var opt = {};
    opt.url = "/Error/FrontEndErrorLog";
    opt.data = { errorMsg: errorMsg };
    send(opt);
};

//api
var api = {};
var _api = function () {

    var api = {};

    /********************* User Begin *********************/
    var user = {};
    api.user = user;
    user.signin = build("/User/SignIn");
    user.signup = build("/User/SignUp");
    user.signout = build("/User/SignOut");


    /********************* User End *********************/

    /********************* Finance Begin *********************/
    var finance = {};
    api.finance = finance;
    finance.getlist = build("/finance/getlist");
    finance.add = build("/finance/add");
    finance.getdetailbyid = build("/finance/getdetailbyid");
    finance.getdetailbyname = build("/finance/getdetailbyname");
    finance.getlocations = build("/finance/getlocations");
    finance.getitemdetails = build("/finance/getitemdetails");

    /********************* Finance End *********************/

    /********************* Hobby Begin *********************/

    var hobby = {};
    api.hobby = hobby;
    //影视
    hobby.getmovielist = build("/Hobby/GetMovieList");
    hobby.deletemovie = build("/Hobby/DeleteMovie");
    hobby.insertmovie = build("/Hobby/InsertMovie");
    hobby.createmovie = build("/Hobby/CreateMovie");
    hobby.updatemovie = build("/Hobby/UpdateMovie");

    //日记
    hobby.creatediary = build("/Hobby/CreateDiary");
    hobby.deletediary = build("/Hobby/DeleteDiary");
    hobby.getdiary = build("/Hobby/GetDiary");
    hobby.getdiarylabels = build("/Hobby/GetDiaryLabels");
    hobby.getdiarycategorys = build("/Hobby/GetDiaryCategorys");
    hobby.getdiarylabelstop5 = build("/Hobby/GetDiaryLabelsTop5");
    hobby.getdiaryinitdata = build("/Hobby/GetDiaryInitData");

    /********************* Hobby End *********************/

    /********************* Search Begin *********************/

    var search = {};
    api.search = search;
    search.savekey = build("/Search/SaveKey");
    search.getkeys = build("/Search/GetKeys");

    /********************* Search End *********************/

    /********************* YRXG Begin *********************/

    var yrxg = {};
    api.yrxg = yrxg;
    yrxg.searchkey = build("/Private/SearchKey");
    yrxg.searchbyid = build("/Private/SearchById");

    /********************* YRXG End *********************/

    /********************* Private Begin *********************/

    var private = {};
    api.private = private;
    private.initpagedata = build("/Private/InitPageData");
    private.addfinancelocation = build("/Private/AddFinanceLocation");
    private.addfinancedetail = build("/Private/AddFinanceDetail");
    private.getstatisticsdetail = build("/Private/GetStatisticsDetail");

    /********************* Private End *********************/

    return api;
};
api = _api();