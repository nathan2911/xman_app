!function(e){"use strict";var a=function(){};
a.prototype.createAreaChart=function(e,a,t,r,i,n,o,s){Morris.Area({element:e,pointSize:0,lineWidth:0,
data:r,xkey:i,ykeys:n,labels:o,hideHover:"auto",resize:!0,gridLineColor:"rgba(108, 120, 151, 0.1)",
lineColors:s})},a.prototype.createStackedChart=function(e,a,t,r,i,n){Morris.Bar({element:e,data:a,xkey:t,
ykeys:r,stacked:!0,labels:i,hideHover:"auto",resize:!0,gridLineColor:"rgba(108, 120, 151, 0.1)",
barColors:n})},a.prototype.init=function()
{this.createAreaChart("morris-area-example",0,0,[{y:"2009",a:10,b:20},{y:"2010",a:75,b:65},
{y:"2011",a:50,b:40},{y:"2012",a:75,b:65},{y:"2013",a:50,b:40},{y:"2014",a:75,b:65},{y:"2015",a:90,b:60}],
"y",["a","b"],["Series A","Series B"],["#3db9dc","#039cfd"]);
this.createStackedChart("morris-bar-stacked",[{y:"2005",a:45,b:180},
{y:"2006",a:75,b:65},{y:"2007",a:100,b:90},{y:"2008",a:75,b:65},
{y:"2009",a:100,b:90},{y:"2010",a:75,b:65},{y:"2011",a:50,b:40},
{y:"2012",a:75,b:65},{y:"2013",a:50,b:40},{y:"2014",a:75,b:65},
{y:"2015",a:100,b:90}],"y",["a","b"],["Series A","Series B"],["#3db9dc","#ebeff2"])},
e.MorrisCharts=new a,e.MorrisCharts.Constructor=a}(window.jQuery),function(e)
{"use strict";window.jQuery.MorrisCharts.init()}();
var chart=new Chartist.Pie("#animating-donut",
{series:[76,1,22,1],labels:[1,2,3,4]},
{donut:!0,showLabel:!1,plugins:[Chartist.plugins.tooltip()]});
chart.on("draw",function(e){if("slice"===e.type)
{var a=e.element._node.getTotalLength();
e.element.attr({"stroke-dasharray":a+"px "+a+"px"});
var t={"stroke-dashoffset":{id:"anim"+e.index,dur:1e3,from:-a+"px",
to:"0px",easing:Chartist.Svg.Easing.easeOutQuint,fill:"freeze"}};
0!==e.index&&(t["stroke-dashoffset"].begin="anim"+(e.index-1)+".end"),
e.element.attr({"stroke-dashoffset":-a+"px"}),e.element.animate(t,!1)}}),
chart.on("created",function(){window.__anim21278907124&&(clearTimeout(window.__anim21278907124),
window.__anim21278907124=null),window.__anim21278907124=setTimeout(chart.update.bind(chart),1e4)});
var data={labels:["W1","W2","W3","W4","W5","W6","W7","W8","W9","W10"],series:[[1,2,4,8,6,-2,-1,-4,-6,-2]]},
options={high:10,low:-10,axisX:{labelInterpolationFnc:function(e,a){return a%2==0?e:null}},
plugins:[Chartist.plugins.tooltip()]};new Chartist.Bar("#bi-polar-bar",data,options),
new Chartist.Line("#chart-with-area",{labels:[1,2,3,4,5,6,7,8],series:[[5,9,7,8,5,3,5,4]]},
{low:0,showArea:!0,plugins:[Chartist.plugins.tooltip()]});
data={series:[8,3]};var sum=function(e,a){return e+a};
new Chartist.Pie("#simple-pie",data,{labelInterpolationFnc:function(e)
{return Math.round(e/data.series.reduce(sum)*100)+"%"}});