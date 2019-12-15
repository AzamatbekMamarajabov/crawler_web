

// variable that keeps all the filter information

var send_data = {}

$(document).ready(function () {
    // reset all parameters on page load

    resetFilters();
    // bring all the data without any filters

    getAPIData();
    // get all websites from database via 

    // AJAX call into website select options

    getWebsites();
    // get all varities from database via 

    // AJAX call into variert select options

    getvariety();

    // on selecting the website option

    $('#websites').on('change', function () {
        // since province and region is dependent 

        // on website select, emty all the options from select input

        $("#province").val("all");
        $("#region").val("all");
        send_data['province'] = '';
        send_data['region'] = '';

        // update the selected website

        if (this.value == "all")
            send_data['website'] = "";
        else
            send_data['website'] = this.value;

        //get province of selected website

        getProvince(this.value);
        // get api data of updated filters

        getAPIData();
    });

    // on filtering the variety input

    $('#variety').on('change', function () {
        // get the api data of updated variety

        if (this.value == "all")
            send_data['variety'] = "";
        else
            send_data['variety'] = this.value;
        getAPIData();
    });

    // on filtering the province input

    $('#province').on('change', function () {
        // clear the region input 

        // since it is dependent on province input

        send_data['region'] = "";
        $('#region').val("all");
        if (this.value == "all")
            send_data['province'] = "";
        else
            send_data['province'] = this.value;
        getRegion(this.value);
        getAPIData();
    });

    // on filtering the region input

    $('#region').on('change', function () {
        if (this.value == "all")
            send_data['region'] = "";
        else
            send_data['region'] = this.value;
        getAPIData();
    });

    // sort the data according to price/points

    $('#sort_by').on('change', function () {
        send_data['sort_by'] = this.value;
        getAPIData();
    });

    // display the results after reseting the filters

    $("#display_all").click(function () {
        resetFilters();
        getAPIData();
    })
})


/**
    Function that resets all the filters   
**/
function resetFilters() {
    $("#websites").val("all");
    $("#province").val("all");
    $("#region").val("all");
    $("#variety").val("all");
    $("#sort_by").val("none");

    //clearing up the province and region select box

    getProvince("all");
    getRegion("all");

    send_data['website'] = '';
    send_data['province'] = '';
    send_data['region'] = '';
    send_data['variety'] = '';
    send_data["sort_by"] = '',
        send_data['format'] = 'json';
}

/**.
    Utility function to showcase the api data 
    we got from backend to the table content
**/
function putTableData(result) {
    // creating table row for each result and

    // pushing to the html cntent of table body of listing table

    let row;
    if (result["results"].length > 0) {
        $("#no_results").hide();
        $("#list_data").show();
        $("#listing").html("");
        $.each(result["results"], function (a, b) {
            row = "<tr> <td>" + b.website + "</td>" +
                "<td>" + b.taster_name + "</td>" +
                "<td title=\"" + b.title + "\">" + b.title.slice(0, 50) + "..." + "</td>" +
                "<td title=\"" + b.description + "\">" + b.description.slice(0, 60) + "..." + "</td>" +
                "<td>" + b.designation + "</td>" +
                "<td>" + b.points + "</td>" +
                "<td>" + b.price + "</td>" +
                "<td>" + b.province + "</td>" +
                "<td>" + b.region + "</td>" +
                "<td>" + b.winery + "</td>" +
                "<td>" + b.variety + "</td></tr>"
            $("#listing").append(row);
        });
    }
    else {
        // if no result found for the given filter, then display no result

        $("#no_results h5").html("No results found");
        $("#list_data").hide();
        $("#no_results").show();
    }
    // setting previous and next page url for the given result

    let prev_url = result["previous"];
    let next_url = result["next"];
    // disabling-enabling button depending on existence of next/prev page. 

    if (prev_url === null) {
        $("#previous").addClass("disabled");
        $("#previous").prop('disabled', true);
    } else {
        $("#previous").removeClass("disabled");
        $("#previous").prop('disabled', false);
    }
    if (next_url === null) {
        $("#next").addClass("disabled");
        $("#next").prop('disabled', true);
    } else {
        $("#next").removeClass("disabled");
        $("#next").prop('disabled', false);
    }
    // setting the url

    $("#previous").attr("url", result["previous"]);
    $("#next").attr("url", result["next"]);
    // displaying result count

    $("#result-count span").html(result["count"]);
}

function getAPIData() {
    let url = $('#list_data').attr("url")
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        beforeSend: function () {
            $("#no_results h5").html("Loading data...");
        },
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            $("#no_results h5").html("Something went wrong");
            $("#list_data").hide();
        }
    });
}

$("#next").click(function () {
    // load the next page data and 

    // put the result to the table body

    // by making ajax call to next available url

    let url = $(this).attr("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            console.log(response)
        }
    });
})

$("#previous").click(function () {
    // load the previous page data and 

    // put the result to the table body 

    // by making ajax call to previous available url

    let url = $(this).attr("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            console.log(response)
        }
    });
})

function getWebsites() {
    // fill the options of websites by making ajax call

    // obtain the url from the websites select input attribute

    let url = $("#websites").attr("url");

    // makes request to getWebsites(request) method in views

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {

            websites_option = "<option value='all' selected>All Websites</option>";
            $.each(result["websites"], function (a, b) {
                websites_option += "<option>" + b + "</option>"
            });
            $("#websites").html(websites_option)
        },
        error: function (response) {
            console.log(response)
        }
    });
}

function getvariety() {
    // fill the options of varities by making ajax call

    // obtain the url from the varities select input attribute

    let url = $("#variety").attr("url");
    // makes request to getvariety(request) method in views

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {
            winery_options = "<option value='all' selected>All Varieties</option>";
            $.each(result["variety"], function (a, b) {
                winery_options += "<option>" + b + "</option>"
            });
            $("#variety").html(winery_options)
        },
        error: function (response) {
            console.log(response)
        }
    });
}

function getProvince(website) {
    // fill the options of provinces by making ajax call

    // obtain the url from the provinces select input attribute

    let url = $("#province").attr("url");
    // makes request to getProvince(request) method in views

    let province_option = "<option value='all' selected>All Provinces</option>";
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            "website": website
        },
        success: function (result) {
            $.each(result["province"], function (a, b) {
                province_option += "<option>" + b + "</option>"
            });
            $("#province").html(province_option)
        },
        error: function (response) {
            console.log(response)
        }
    });
}

function getRegion(province) {
    // fill the options of region by making ajax call

    // obtain the url from the region select input attribute

    let url = $("#region").attr("url");
    // makes request to getRegion(request) method in views

    let region_option = "<option value='all' selected>All regions</option>";
    $.ajax({
        method: 'GET',
        url: url,
        data: {
            "province": province
        },
        success: function (response) {
            $.each(response["region"], function (a, b) {
                region_option += "<option>" + b + "</option>"
            });
            $("#region").html(region_option);
        },
        error: function (response) {
            console.log(response)
        }
    });
}

