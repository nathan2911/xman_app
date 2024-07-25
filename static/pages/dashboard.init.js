!function(a){"use strict";
    var e=function(){};
    e.prototype.createStackedChart=function(a,e,r,t,o,c)
    {
    Morris.Bar({element:a,data:e,xkey:r,
    ykeys:t,stacked:!0,
    labels:o,
    hideHover:"auto",
    barSizeRatio:.4,
    resize:!0,
    gridLineColor:"rgba(108, 120, 151, 0.1)",
    barColors:c})},
    e.prototype.createDonutChart=function(a,e,r)
    {Morris.Donut({element:a,data:e,resize:!0,colors:r})},
    e.prototype.init=function()
    {this.createStackedChart("morris-bar-stacked",
        [{y:"2011",a:45,},
        {y:"2012",a:75,},
        {y:"2013",a:100,},
        {y:"2014",a:75,},
        {y:"2015",a:100,},
        {y:"2016",a:75,},
        {y:"2017",a:50,},
        {y:"2018",a:75,},
        {y:"2019",a:50,},
        {y:"2020",a:75,},
        {y:"2021",a:100,}],
        "y",["a",],
        [".",],
        ["#b9f2ff"]);
        this.createDonutChart("morris-donut-example",
            [{label:"Gold",value:35},
            {label:"Diamond",value:29},
            {label:"Platinum",value:22},
            {label:"Others",value:14}],
            ["#FFD700","#b9f2ff","#E5E4E2", "#006400"])},
            a.Dashboard=new e,a.Dashboard.Constructor=e}
            (window.jQuery),function(a){"use strict";
            window.jQuery.Dashboard.init()}();