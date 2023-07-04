$(document).ready(function () {
    // $("button").click(function () {
    //     alert("666")
    // });
});

function download_file() {
    var a = document.createElement("a");
    a.href = "/download_flie?name=肖舒翔&age=26&marry=false";
    a.download = "文件名2.pdf";
    a.click();
}

function data_transport() {
    var params = JSON.stringify({
        name: "肖舒翔",
        age: 26,
        maray: false
    });
    $.ajax({
        type: "POST",
        url: "/get_post/",
        dataType: "JSON",
        contentType: "application/json;charset=utf-8",
        data: params,
        success: function (data) {
            alert(data.name);
        },
        error: function (data, status, e) {
            alert("错误！" + status + e)
        }
    })
}

function up_file() {
    var formData = new FormData($("#formSubmit")[0]);
    $.ajax({
        async: false,
        type: "POST",
        url: "/up_file/",
        data: formData,
        dataType: "JSON",
        mimeType: "multipart/form-data",
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            alert("上传成功！");
        },
        error: function (data, status, e) {
            alert("上传出现错误！请联系管理员");
        }
    });
    return false;
}
