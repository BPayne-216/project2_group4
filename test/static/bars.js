// Step 1: Set up our chart
//= ================================

var margin = {top: 20, right: 40, bottom: 60, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;


// parse the date / time
var parseTime = d3.timeParse("%Y");

// set the ranges
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

// define the 1st line
var valueline = d3.line()
    .x(function(d) { return x(d.year); })
    .y(function(d) { return y(d.USA); });

// define the 2nd line
var valueline2 = d3.line()
    .x(function(d) { return x(d.year); })
    .y(function(d) { return y(d.China); });

// define the 3rd line
var valueline3 = d3.line()
    .x(function(d) { return x(d.year); })
    .y(function(d) { return y(d.Russia); });

// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("dummy1.csv").then(function(data) {

  // format the data
  data.forEach(function(d) {
      d.year = parseTime(d.year);
      d.USA = +d.USA;
      d.China = +d.China;
      d.Russia = +d.Russia;
  });

  // Scale the range of the data
  x.domain(d3.extent(data, function(d) { return d.year; }));
  y.domain([0, d3.max(data, function(d) {
	  return Math.max(d.USA, d.China, d.Russia); })]);

  // Add the valueline path.
  svg.append("path")
      .data([data])
      .attr("class", "line")
      .attr("d", valueline);

  // Add the valueline2 path.
  svg.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke", "red")
      .attr("d", valueline2);

  // Add the valueline2 path.
  svg.append("path")
      .data([data])
      .attr("class", "line")
      .style("stroke", "blue")
      .attr("d", valueline3);

  // Add the X Axis
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));
  
  // text label for the x axis
  svg.append("text")             
      .attr("transform",
            "translate(" + (width/2) + " ," + (height + margin.top + 20) + ")")
      .style("text-anchor", "middle")
      .text("Year");

  // Add the Y Axis
  svg.append("g")
      .call(d3.axisLeft(y));

  // text label for the y axis
  svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x",0 - (height / 2))
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text("Country");    

});
