<style>
#program, #program th, #program td {
    border: 1px solid gray;
    font-size: 85%;
    border-collapse: separate;
    border-spacing: 1px;
    color: #222222;
}
@media (min-width: 1200px) {
    #program {
        margin-left: -50px;
        margin-right: -50px;
    }
}
#program th, #program td {
  padding: 5px;
  text-align: left;
}
#hide-show-timezones {
    font-size: 90%;
    margin-top: 1em;
    padding: 0 6px;
    display: flex;
    flex: 0 0 auto;
    flex-direction: row;
    flex-wrap: wrap;
    white-space: nowrap;
    justify-content: space-between;
}
#hide-show-timezones input.largerCheckbox {
    transform : scale(1.5);
}
#hide-show-timezones label {
    padding: 0 4px 0 8px;
}
#program div, #program a {
    color: white;
}
#program a:hover {
    text-decoration: underline;
}
#r00{
      background-color: #96B6BD;
 /*   appearance: none;*/
    box-shadow: 0 0 0px 8px gold;

  clip-path: polygon(-20% 0%, 100% 0%, 100% 100%, -20% 100%); /*left*/

}
#r00t{
      background-color: #96B6BD;
        box-shadow: 0 0 0px 8px gold;
        clip-path: polygon(-20% -20%, 100% -20%, 100% 100%, -20% 100%); /*top-left*/
    }


#t01b {
  background-color: #BDC0BF;
    box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
  font-weight: 350
}

#t01t {
  background-color: #BDC0BF;
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
  font-weight: 350
}
#r00b{
      background-color: #96B6BD;
        box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(-20% 0%, 100% 0%, 100% 120%, -20% 120%); /*bottom--*/
    }

#r01 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #BDC0BF;
  font-weight: 350

}

#r05 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #C4DFB3;
}

#r06 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #F9D368;
}

#r02 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #D9A9BC;
}
#r03 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #CDDFF0;
}
#t00 {
  background-color: #96B6BD;
}
#t01 {
  background-color: #BDC0BF;
  font-weight: 350
}

#cshort_v {
  background-color: #B9A3BE;
}
#clong_v {
  background-color: #B8CEDB;
}

#cmentor {
  background-color: #E8B8A2;
}
#cspecial {
  background-color: #74A1A7;
}
    #cspecial_t{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
      border: 1px;}
     #cspecial_tr{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 120% -20%, 120% 100%, 0% 100%); /*top-right*/
      border: 1px;}
    #cspecial_br{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 120%, 0% 120%); /*bottom-right*/
      border: 1px;}

    #cspecial_b{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
      border: 1px;}

    #title_legend{font-weight:300; font-size: 100%; text-align:left; color:white; padding-left: 6px; padding-right: 6px; white-space: nowrap; }
    #text_legend{font-weight:150; font-size: 80%; text-align:left; padding-left: 6px; }
    #cbreak_r{   background-color: #AEAEAE; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cbreak{   background-color: #AEAEAE; }
    #cbreak div, #cbreak_r div { color: #222222; } 

    #clong_tr{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 120% -20%, 120% 100%, 0% 100%); /*top-right*/
      border: 1px;}

    #clong_t{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
      border: 1px;}

    #clong_r{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #clong{   background-color: #0083AC;}

    #ckeynote_r{   background-color: #016297; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #ckeynote{   background-color: #016297;}

    #cshort_r{   background-color: #82538B; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cshort{   background-color: #82538B;}

    #cposter_r{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cposter_br{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 120%, 0% 120%); /*bottom-right*/
      border: 1px;}

    #cposter_b{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
      border: 1px;}

    #cposter{   background-color: #248F85;}


</style>

<script>
jQuery(document).ready(function($) {
    $('input[type= checkbox ]').click(function() {
        let index = $(this).attr('name').substr(3);
        index--;
        $('table tr').each(function() {
            $('td:eq(' + index + ')',this).toggle();
        });
        $('th.' + $(this).attr('name')).toggle();
    });
});
</script>
<!--
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
      clip-path: polygon(0% -20%, 100% -20%, 100% 120%, 0% 120%); /*bottom-top*/
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
  clip-path: polygon(0% 0%, 120% 0%, 120% 120%, 0% 120%); /*bottom-right*/
-->

{% from "_macros.html" import paper %}

# Program at a Glance

<table id="program"><thead><tr><th class='col1' id='t01'>PDT UTC-7</th><th class='col2' id='t01'>EDT UTC-4</th><th class='col3' id='t00'>L&uuml;beck UTC+2</th><th class='col4' id='t01'>HKT UTC+8</th><th colspan='2' id='t00'><b>Wednesday 7th July</b></th><th colspan='2' id='t00'><b>Thursday 8th July</b></th><th colspan='2' id='t00'><b>Friday 9th July</b></th></thead>
<tr><th id='t01' class='col1'>00:00</th><th id='t01' class='col2'>3:00</th><th id='t00' class='col3'>9:00</th><th id='t01' class='col4'>15:00</th><th id='cshort_v'><a href='#shortA'>A4-12</a> Videos</th><th id='cshort_v'><a href='#shortB'>B1-9</a> Videos</th><th id='cshort_v'><a href='#shortE'>E4-12</a> Videos</th><th id='cshort_v'><a href='#shortF'>F1-9</a> Videos</th><th id='cshort_v'><a href='#shortI'>I4-12</a> Videos</th><th id='cshort_v'><a href='#shortJ'>J1-9</a> Videos</th>

<tr><th id='t01' class='col1' >00:45</th><th id='t01' class='col2'>3:45</th><th id='t00' class='col3'>9:45</th><th id='t01' class='col4'>15:45</th><th colspan='2' id='clong_v'><a href='#longA'>A1-3</a> Long Videos</th><th colspan='2' id='clong_v'><a href='#longE'>E1-3</a> Long Videos</th><th colspan='2' id='clong_v'><a href='#longI'>I1-3</a> Long Videos</th>
<tr><th id='t01' class='col1' >01:20</th><th id='t01' class='col2'>4:20</th><th id='t00' class='col3'>10:20</th><th id='t01' class='col4'>16:20</th><th colspan='2' id='t01'>Break / GatherTown</th><th colspan='2' id='t01'>Break / GatherTown</th><th colspan='2' id='t01'>Break / GatherTown</th>
<tr><th id='t01' class='col1'>01:30</th><th id='t01' class='col2'>4:30</th><th id='t00' class='col3'>10:30</th><th id='t01' class='col4'>16:30</th><th id='cshort_v'><a href='#shortC'>C1-9</a> Videos</th><th id='cshort_v'><a href='#shortD'>D4-12</a> Videos</th><th id='cshort_v'><a href='#shortG'>G1-9</a> Videos</th><th id='cshort_v'><a href='#shortH'>H4-12</a> Videos</th><th id='cshort_v'><a href='#shortK'>K1-9</a> Videos</th><th id='cshort_v'><a href='#shortL'>L4-12</a> Videos</th>

<tr><th id='t01' class='col1' >02:15</th><th id='t01' class='col2'>5:15</th><th id='t00' class='col3'>11:15</th><th id='t01' class='col4'>17:15</th><th colspan='2' id='clong_v'><a href='#longD'>D1-3</a> Long Videos</th><th colspan='2' id='clong_v'><a href='#longH'>H1-3</a> Long Videos</th><th colspan='2' id='clong_v'><a href='#longL'>L1-3</a> Long Videos</th>
<tr><th id='t01' class='col1' >02:45</th><th id='t01' class='col2'>5:45</th><th id='t00' class='col3'>11:45</th><th id='t01' class='col4'>17:45</th><th colspan='2' id='cmentor'>Study groups with Mentors (optional)</th><th colspan='2' id='cmentor'>Study groups with Mentors (optional)</th><th colspan='2' id='cmentor'>Study groups with Mentors (optional)</th>
<tr><th id='t01' class='col1' >03:30</th><th id='t01' class='col2'>6:30</th><th id='r00t' class='col3'>12:30</th><th id='t01t' class='col4'>18:30</th><th colspan='2' id='cspecial_t'>Conference Opening</th><th colspan='2' id='cspecial_t'>Industry and Sponsor Event<br />Qualcomm, GE Healthcare, BioMedTec</th><th colspan='2' id='cspecial_tr'>Industry and Sponsor Event<br />UKSH<br /></th>


<tr><th id='t01' class='col1' >04:00</th><th id='t01' class='col2'>7:00</th><th id='r00' class='col3'>13:00</th><th id='t01' class='col4'>19:00</th><th colspan='2' id='clong'><a href='#longA' style='color:white'><b>Long Oral A1-3 Segmentation</b></a> </th><th colspan='2' id='clong'><a href='#longE' style='color:white'><b>Long Oral E1-3 Detection and Diagnosis</b></a> </th><th colspan='2' id='clong_r'><a href='#longI' style='color:white'><b>Long Oral I1-3 Interpretability and Explainable AI</b></a></th>



<tr><th id='t01' class='col1' >04:30</th><th id='t01' class='col2'>7:30</th><th id='r00' class='col3'>13:30</th><th id='t01' class='col4'>19:30</th><th colspan='2' id='cbreak'><div>Break: Meet in GatherTown</div></th><th colspan='2' id='cbreak'><div>Break: Meet in GatherTown</div></th><th colspan='2' id='cbreak_r'><div>Break: Meet in GatherTown</div></th>
<tr><th id='t01' class='col1'>04:45</th><th id='t01' class='col2'>7:45</th><th id='r00' class='col3'>13:45</th><th id='t01' class='col4'>19:45</th><th id='cshort'><a href='#shortA' style='color:white'><b>Short Oral A4-12 Segmentation</b></a></th><th id='cshort'><a href='#shortB' style='color:white'><b>Short Oral B1-9 Histopathology</b></a></th><th id='cshort'><a href='#shortE' style='color:white'><b>Short Oral E4-12 Image Registration / Synthesis</b></a></th><th id='cshort'><a href='#shortF' style='color:white'><b>Short Oral F1-9 Imaging: Reconstruction and Clinical Data</b></a></th><th id='cshort'><a href='#shortI' style='color:white'><b>Short Oral I4-12 Transfer Learning and Domain Adaptation </b></a></th><th id='cshort_r'><a href='#shortJ' style='color:white'><b>Short Oral J1-9 Unsupervised and Representation Learning </b></a></th>



<tr><th id='t01' class='col1' >05:30</th><th id='t01' class='col2'>8:30</th><th id='r00' class='col3'>14:30</th><th id='t01' class='col4'>20:30</th><th colspan='2' id='cposter'><div>Individual virtual poster rooms (21 papers)</div></th><th colspan='2' id='cposter'><div>Individual virtual poster rooms (21 papers)</div></th><th colspan='2' id='cposter_r'><div>Individual virtual poster rooms (21 papers)</div></th>


<tr><th id='t01' class='col1' >06:00</th><th id='t01' class='col2'>9:00</th><th id='r00' class='col3'>15:00</th><th id='t01' class='col4'>21:00</th><th colspan='2' id='cbreak'><div>Break: Meet in GatherTown</div></th><th colspan='2' id='cbreak'><div>Break: Meet in GatherTown</div></th><th colspan='2' id='cbreak_r'><div>Break: Meet in GatherTown</div></th>


<tr><th id='t01' class='col1' >06:15</th><th id='t01' class='col2'>9:15</th><th id='r00' class='col3'>15:15</th><th id='t01' class='col4'>21:15</th><th colspan='2' id='ckeynote'><div><a href="https://youtu.be/lK9IIW9GcPw" style='color:white'>Keynote - Polina Golland</a></div></th><th colspan='2' id='ckeynote'><div><a href="https://youtu.be/lXBIBS-2iBk" style='color:white'>Keynote - Bernhard Schölkopf</a></div></th><th colspan='2' id='ckeynote_r'><div>Keynote - Bernd Stahl</div></th>




<tr><th id='t01' class='col1' >07:00</th><th id='t01' class='col2'>10:00</th><th id='r00' class='col3'>16:00</th><th id='t01' class='col4'>22:00</th><th colspan='2' id='clong'><a href='#longD' style='color:white'><b>Long Oral D1-3 Unsupervised and Representation Learning</b></a></th><th colspan='2' id='clong'><a href='#longH' style='color:white'><b>Long Oral H1-3 Image Acquisition and Reconstruction</b></a></th><th colspan='2' id='clong_r'><a href='#longL' style='color:white'><b>Long Oral L1-3 Learning with Noisy Labels and Limited Data</b></a></th>



    <tr><th id='t01' class='col1' >07:30</th><th id='t01' class='col2'>10:30</th><th id='r00' class='col3'>16:30</th><th id='t01' class='col4'>22:30</th><th colspan='2' id='cbreak'><div>Break: Meet in GatherTown</div></th><th colspan='2' id='cbreak'><div>Break: Meet in GatherTown</div></th><th colspan='2' id='cbreak_r'><div>Break: Meet in GatherTown</div></th>

<tr><th id='t01' class='col1'>07:45</th><th id='t01' class='col2'>10:45</th><th id='r00' class='col3'>16:45</th><th id='t01' class='col4'>22:45</th><th id='cshort'><a href='#shortC' style='color:white'><b>Short Oral C1-9 Endoscopy and Validation Studies</b></a></th><th id='cshort'><a href='#shortD' style='color:white'><b>Short Oral D4-12 Detection and Diagnosis 1</b></a></th><th id='cshort'><a href='#shortG' style='color:white'><b>Short Oral G1-9 Interpretability and Explainable AI</b></a></th><th id='cshort'><a href='#shortH' style='color:white'><b>Short Oral H4-12 Application: Radiology</b></a> </th><th id='cshort'><a href='#shortK' style='color:white'><b>Short Oral K1-9 Learning with Noisy Labels and Limited Data</b></a> </th><th id='cshort_r'><a href='#shortL' style='color:white'><b>Short Oral L4-9 Detection and Diagnosis 2</b></a> </th>





    <tr><th id='t01' class='col1' >08:30</th><th id='t01' class='col2'>11:30</th><th id='r00' class='col3'>17:30</th><th id='t01' class='col4'>23:30</th><th colspan='2' id='cposter'><div>Individual virtual poster rooms (21 papers)</div></th><th colspan='2' id='cposter'><div>Individual virtual poster rooms (21 papers)</div></th><th colspan='2' id='cposter_r'><div>Individual virtual poster rooms (21 papers)</div></th>





<tr><th id='t01' class='col1' >09:00</th><th id='t01' class='col2'>12:00</th><th id='r00b' class='col3'>18:00</th><th id='t01b' class='col4'>0:00</th><th colspan='2' id='cspecial_b'>Industry and Sponsor Event<br />Qualcomm, Heartflow, PaigeAI, UKSH</th><th colspan='2' id='cspecial_b'>Industry and Sponsor Event<br />SnkeOS, Heartflow, PaigeAI, BioMedTec</th><th colspan='2' id='cspecial_br'>Closing</th>

<tr><th id='t01' class='col1' >09:45</th><th id='t01' class='col2'></th><th id='t00' class='col3'>18:45</th><th id='t01' class='col4'></th><th colspan='2' id='t01'>Break / GatherTown</th><th colspan='2' id='t01'>Break / GatherTown</th><th colspan='2'></th>
<tr><th id='t01' class='col1' >10:00</th><th id='t01' class='col2'>13:00</th><th id='t00' class='col3'>19:00</th><th id='t01' class='col4'>1:00</th><th colspan='2' id='t07'>Virtual Social Event / Drinks</th><th colspan='2' id='t07'>Virtual Gala Evening</th><th colspan='2'></th>

<tr><th id='t01' class='col1'>12:00</th><th id='t01' class='col2'>15:00</th><th id='t00' class='col3'>21:00</th><th id='t01' class='col4'>3:00</th><th id='cshort_v'><a href='#shortE'>E4-12</a>  Videos</th><th id='cshort_v'><a href='#shortF'>F1-9</a> Videos</th><th id='cshort_v'><a href='#shortI'>I4-12</a> Videos</th><th id='cshort_v'><a href='#shortJ'>J1-9</a> Videos</th><th colspan='2'></th>

<tr><th id='t01' class='col1' >12:45</th><th id='t01' class='col2'>15:45</th><th id='t00' class='col3'>21:45</th><th id='t01' class='col4'>3:45</th><th colspan='2' id='clong_v'><a href='#longE'>E1-3</a> Long Videos</th><th colspan='2' id='clong_v'><a href='#longI'>I1-3</a> Long Videos</th><th colspan='2'></th>
<tr><th id='t01' class='col1' >13:20</th><th id='t01' class='col2'>16:20</th><th id='t00' class='col3'>22:20</th><th id='t01' class='col4'>4:20</th><th colspan='2' id='t01'>Break / GatherTown</th><th colspan='2' id='t01'>Break / GatherTown</th><th colspan='2'></th>
<tr><th id='t01' class='col1'>13:30</th><th id='t01' class='col2'>16:30</th><th id='t00' class='col3'>22:30</th><th id='t01' class='col4'>4:30</th><th id='cshort_v'><a href='#shortG'>G1-9</a>  Videos</th><th id='cshort_v'><a href='#shortH'>H4-12</a>  Videos</th><th id='cshort_v'><a href='#shortK'>K1-9</a> Videos</th><th id='cshort_v'><a href='#shortL'>L4-12</a> Videos</th><th colspan='2'></th>

<tr><th id='t01' class='col1' >14:15</th><th id='t01' class='col2'>17:15</th><th id='t00' class='col3'>23:15</th><th id='t01' class='col4'>5:15</th><th colspan='2' id='clong_v'><a href='#longH'>H1-3</a> Long Videos</th><th colspan='2' id='clong_v'><a href='#longL'>L1-3</a> Long Videos</th><th colspan='2'></th>
<tr><th id='t01' class='col1' >14:45</th><th id='t01' class='col2'>17:45</th><th id='t00' class='col3'>23:45</th><th id='t01' class='col4'>5:45</th><th colspan='2' id='cmentor'>Study groups with Mentors (optional) Americas (for 45 min)</th><th colspan='2' id='cmentor'>Study groups with Mentors (optional) Americas (for 45 min)</th><th colspan='2'></th> </table>

<form id="hide-show-timezones">
    <div>
        <input class="largerCheckbox" type="checkbox" id="hs-col1" name="col1" checked="checked">
        <label for="hs-col1">Hide/Show UTC-7</label>
    </div>
    <div>
        <input class="largerCheckbox" type="checkbox" id="hs-col2" name="col2" checked="checked">
        <label for="hs-col2">Hide/Show UTC-4</label>
    </div>
    <div>
        <input class="largerCheckbox" type="checkbox" id="hs-col3" name="col3" checked="checked">
        <label for="hs-col3">Hide/Show UTC+2</label>
    </div>
    <div>
        <input class="largerCheckbox" type="checkbox" id="hs-col4" name="col4" checked="checked">
        <label for="hs-col4">Hide/Show UTC+8</label>
    </div>
</form>

<hr>

## Legend

<table>
<tr><th id='clong_v'><div id="title_legend">Long Videos</div></th><th><div id="text_legend">Passive viewing of long oral videos (10-13 minutes each).<br> Questions in chat are collected for later live discussion.</div></th>
    <tr><th id='clong'><div id="title_legend">Long Oral Discussion</div></th><th><div id="text_legend"><b>(max.) 3</b> minute introduction of each speaker/paper<br> followed by 21 minute discussion (group of 3)</div></th>
<tr><th id='cshort_v'><div id="title_legend">Short Videos</div></th><th><div id="text_legend">Passive viewing of short oral videos (4-6 minutes each).<br> Dual Track. Questions in chat are collected for later live discussion.</div></th>
<tr><th id='cshort'><div id="title_legend">Short Oral Discussion</div></th><th><div id="text_legend">Split into three consecutive groups of 3. <b>(max.) 90 second</b> introduction<br> of each speaker/paper followed by 10.5 minute discussion (group of 3). Dual Track.</div></th>
    <tr><th id='cposter'><div id="title_legend">Individual Poster Rooms</div></th><th><div id="text_legend">Virtual poster session in GatherTown (all papers of preceeding sessions)<br> Preview of poster PDF (slide) and ad-hoc video chat with presenters (other attendees) </div></th>
<tr><th id='ckeynote'><div id="title_legend">Keynote</div></th><th><div id="text_legend">Live (virtual) presentation with following discussion in Webinar. </div></th>

<tr><th id='cspecial'><div id="title_legend">Industry and Sponsors</div></th><th><div id="text_legend">Virtual booth and videos presenting supporting companies.<br>Networking and career opportunities. </div></th>
<tr><th id='cmentor'><div id="title_legend">Study Groups / Mentors</div></th><th><div id="text_legend">(optional with prior sign-up: <a href="https://forms.gle/CNPTBZQ4fzWuFKY6A">Google Form</a>). Study groups assemble questions<br> for live discussion. Meet in deticated study rooms and also get great advice from mentors. </div></th>
<tr><th id='cbreak'><div id="title_legend">Breaks: GatherTown</div></th><th><div id="text_legend">Meet new and old colleagues for ad-hoc (video) chats on the hallway<br>or in free meeting spaces. Have coffee or enjoy views over L&uuml;beck. </div></th>

        </table>

---

Since the program of this years MIDL might appear quite differently from what you expect, there is a [video](https://youtu.be/Nlzt1LgOubc) explaining how you can enjoy the scientific presentations and discussions throughout the conference!

We gave our best to give every participant the opportunity for live interaction with the authors, regardless of the timezone. Therefore, each conference day is divided into two parts: The active part and the passive part.
The active part - the <b>prime time</b> - takes place in the time frame that is most convenient across all time zones and is marked in yellow.

During this active part, live spotlight presentations of and discussions with the authors of all accepted papers are scheduled. Additionally, the keynotes, virtual poster sessions as well as social events will take place during the active phase. Hence, participants from all over the world get the chance to discuss the presented research, meet new colleagues and old friends, and enjoy a live virtual event.

In the passive part, the full presentation videos of all accepted papers are shown in moderated sessions. Each presentation is streamed twice to address the different time zones, once the day before after the active phase and once right before the active phase where the paper is discussed. Questions that arise during these sessions will be collected and answered in the corresponding discussion session during the active phase. All presentation videos will also be accessible on the homepage so that they can also be enjoyed outside the moderated sessions.

---
<h2> Wednesday 7th July</h2>
<a id="longA"></a><h3>A1-3 (long): Segmentation - 13:00 - 13:30 (UTC+2)</h3>
Chairs: Minjeong Kim, Jelmer Wolterink <br>
[% .papers %]
{{ paper('Whole-Body Soft-Tissue Lesion Tracking and Segmentation in Longitudinal CT Imaging Studies',
        'Alessa Hering, Felix Peisen, Teresa Amaral, Sergios Gatidis, Thomas Eigentler, Ahmed Othman, Jan Hendrik Moltz',
        openreview='https://openreview.net/forum?id=hzbuHGhU02Z',
        pdf='/proceedings/hering21.pdf',
        id='A1',
        paper='papers/A1.html',
        proceedings='',
        abstract='In follow-up CT examinations of cancer patients, therapy success is evaluated by estimating the change in tumor size. This process is time-consuming and error-prone. We present a pipeline that automates the segmentation and measurement of matching lesions, given a point annotation in the baseline lesion. First, a region around the point annotation is extracted, in which a deep-learning-based segmentation of the lesion is performed. Afterward, a registration algorithm finds the corresponding image region in the follow-up scan and the convolutional neural network segments lesions inside this region. In the final step, the corresponding lesion is selected. We evaluate our pipeline on clinical follow-up data comprising 125 soft-tissue lesions from 43 patients with metastatic melanoma. Our pipeline succeeded for 96% of the baseline and 80% of the follow-up lesions, showing that we have laid the foundation for an efficient quantitative follow-up assessment in clinical routine.')
}}
{{ paper('Embedding-based Instance Segmentation in Microscopy',
        'Manan Lalit, Pavel Tomancak, Florian Jug',
        openreview='https://openreview.net/forum?id=JM6GuFGayL5',
        pdf='/proceedings/lalit21.pdf',
        id='A2',
        paper='papers/A2.html',
        proceedings='',
        abstract='Automatic detection and segmentation of objects in 2D and 3D microscopy data is important for countless biomedical applications.In the natural image domain, spatial embedding-based instance segmentation methods are known to yield high-quality results, but their utility for segmenting microscopy data is currently little researched. Here we introduce EmbedSeg, an embedding-based instance segmentation method which outperforms existing state-of-the-art baselines on 2D as well as 3D microscopy datasets.Additionally, we show that EmbedSeg has a GPU memory footprint small enough to train even on laptop GPUs, making it accessible to virtually everyone. Finally, we introduce four new 3D microscopy datasets, which we make publicly available alongside ground truth training labels. Our open-source implementation is available at https://github.com/juglab/EmbedSeg.')
}}
{{ paper('Beyond pixel-wise supervision: semantic segmentation with higher-order shape descriptors',
        'Hoel Kervadec, Houda Bahig, Laurent Letourneau-Guillon, Jose Dolz, Ismail Ben Ayed',
        openreview='https://openreview.net/forum?id=nqe6e0oJ_fL',
        pdf='/proceedings/kervadec21.pdf',
        id='A3',
        paper='papers/A3.html',
        proceedings='',
        abstract="Standard losses for training deep segmentation networks could be seen as individual classifications of pixels, instead of supervising the global shape of the predicted segmentations. While effective, they require exact knowledge of the label of each pixel in an image. This study investigates how effective global geometric shape descriptors could be, when used on their own as segmentation losses for training deep networks. Not only interesting theoretically, there exist deeper motivations to posing segmentation problems as a reconstruction of shape descriptors: First, annotations to obtain approximations of low-order shape moments could be much less cumbersome than their full-mask counterparts, and anatomical priors could be readily encoded into invariant shape descriptions, which might alleviate the annotation burden. Also, some shape descriptors could be readily used to encode\\'\\' biomarkers, leading to better interpretability. Finally, and most importantly, we hypothesize that, given a task, certain shape descriptions might be invariant across image acquisition protocols/modalities and subject populations, which might open interesting research avenues for generalization in medical image segmentation.We introduce and formulate a few shape descriptors in the context of deep segmentation, and evaluate their potential as stand-alone losses on two different, challenging tasks. Inspired by recent works in constrained optimization for deep networks, we propose a way to use those descriptors to supervise segmentation, without any pixel-level label. Very surprisingly, as little as 4 descriptors values per class can approach the performance of a segmentation mask with 65k individual discrete labels. We also found that shape descriptors can be a valid way to encode anatomical priors about the task, enabling to leverage expert knowledge without requiring additional annotations. Our implementation is publicly available and can be easily extended.")
}}
[% / %]
<a id="shortA"></a><h3>A4-12 (short): Segmentation - 13:45 - 14:30 (UTC+2)</h3>
Chairs: Francesco Caliva, Christian Desrosiers <br>
[% .papers %]
{{ paper('Common limitations of performance metrics in biomedical image analysis',
        'Annika Reinke, Matthias Eisenmann, Minu Dietlinde Tizabi, Carole H. Sudre, Tim Rädsch, Michela Antonelli, Tal Arbel, Spyridon Bakas, M. Jorge Cardoso, Veronika Cheplygina, Keyvan Farahani, Ben Glocker, Doreen Heckmann-Nötzel, Fabian Isensee, Pierre Jannin, Charles Kahn, Jens Kleesiek, Tahsin Kurc, Michal Kozubek, Bennett A. Landman, Geert Litjens, Klaus Maier-Hein, Anne Lousise Martel, bjoern menze, Henning Müller, Jens Petersen, Mauricio Reyes, Nicola Rieke, Bram Stieltjes, Ronald M. Summers, Sotirios A. Tsaftaris, Bram van Ginneken, Annette Kopp-Schneider, Paul Jäger, Lena Maier-Hein',
        openreview='https://openreview.net/forum?id=76X9Mthzv4X',
        pdf='https://openreview.net/pdf?id=76X9Mthzv4X',
        id='A4',
        paper='papers/A4.html',
        proceedings='',
        abstract="While the importance of automatic biomedical image analysis is increasing at an enormous pace, recent meta-research revealed major flaws with respect to algorithm validation. Performance metrics are key for objective, transparent and comparative performance assessment, but little attention has been given to their pitfalls. Under the umbrella of the Helmholtz Imaging Platform (HIP), three international initiatives - the MICCAI Society\\'s challenge working group, the Biomedical Image Analysis Challenges (BIAS) initiative, as well as the benchmarking working group of the MONAI framework - have now joined forces with the mission to generate best practice recommendations with respect to metrics in medical image analysis. Consensus building is achieved via a Delphi process, a popular tool for integrating opinions in large international consortia. The current document serves as a teaser for the results presentation and focuses on the pitfalls of the most commonly used metric in biomedical image analysis, the Dice Similarity Coefficient (DSC), in the categories of (1) mathematical properties/edge cases, (2) task/metric fit and (3) metric aggregation. Being compiled by a large group of experts from more than 30 institutes worldwide, we believe that our framework could be of general interest to the MIDL community and will improve the quality of biomedical image analysis algorithm validation. ")
}}
{{ paper('VinDr-RibCXR: A Benchmark Dataset for Automatic Segmentation and Labeling of Individual Ribs on Chest X-rays',
        'Hoang Canh Nguyen, Tung Thanh Le, Hieu Pham, Ha Quy Nguyen',
        openreview='https://openreview.net/forum?id=oJi6xpSLdsj',
        pdf='https://openreview.net/pdf?id=oJi6xpSLdsj',
        id='A5',
        paper='papers/A5.html',
        proceedings='',
        abstract='Segmenting and labeling correctly the individual ribs from chest radiograph (CXR) are of significant clinical value for several diagnostic tasks. Developing automatic deep learning (DL) algorithms for this task requires annotated images of the ribs at pixel-level. However, to the best of our knowledge, there exists no such public datasets as well as benchmark protocols for performance evaluation. To solve this problem, we establish a new CXR dataset, namely VinDr-RibCXR, for automatically segmenting and labeling of individual ribs. The VinDr-RibCXR contains 245 posteroanterior CXRs with corresponding segmentation annotations for each rib provided by human experts. Furthermore, we train the state-of-the-art DL-based segmentation models on 196 images from the RibCXR and report performance of those models on an independent test set of 49 images. Our best performing DL model (i.e., Nested U-Net with EfficientNet-B0)  obtains  a  Dice  score  of  0.834 (95% CI, 0.810-0.853). The  sensitivity,  specificity  and  Hausdorff distance are 0.841 (95% CI, 0.812-0.858), 0.998 (95% CI, 0.997-0.998), and 15.453 (95% CI, 13.340-17.450), respectively. These results demonstrate a high-level of performance in labeling of the individual ribs from CXRs. Our study, therefore, serves as a proof of concept and baseline performance for future research. The dataset, codes, and trained DL models will be made publicly available to encourage new advances in this research direction.')
}}
{{ paper('Learning to predict cutting angles from histological human brain sections',
        'Christian Schiffer, Luisa Schuhmacher, Katrin Amunts, Timo Dickscheid',
        openreview='https://openreview.net/forum?id=9CSM4yQmZiN',
        pdf='https://openreview.net/pdf?id=9CSM4yQmZiN',
        id='A6',
        paper='papers/A6.html',
        proceedings='',
        abstract='Studying brain architecture at the cellular level requires histological image analysis of sectioned postmortem samples. We trained a deep neural network to estimate relative angles between the cutting plane and the local 3D brain surface from 2D cortical image patches sampled from microscopic scans of human brain tissue sections. The model allows to automatically identify obliquely cut tissue parts, which often confuse downstream texture classification tasks and typically require specific treatment in image analysis workflows. It has immediate applications for the automated analysis of brain structures, like cytoarchitectonic mapping of the highly convoluted human brain.')
}}
{{ paper('Localizing neurosurgical instruments across domains and in the wild',
        'Markus Philipp, Anna Alperovich, Marielena Gutt-Will, Andrea Mathis, Stefan Saur, Andreas Raabe, Franziska Mathis-Ullrich',
        openreview='https://openreview.net/forum?id=21m0dBCMdd',
        pdf='/proceedings/philipp21.pdf',
        id='A7',
        paper='papers/A7.html',
        proceedings='',
        abstract='Towards computer-assisted neurosurgery, robust methods for instrument localization on neurosurgical microscope video data are needed. Specifically for neurosurgical data, challenges arise from visual conditions such as strong blur and from an unknowingly large variety of instrument types. For neurosurgical domain, instrument localization methods must generalize across different sub-disciplines such as cranial tumor and aneurysm surgeries which exhibit different visual properties. We present and evaluate a methodology towards robust instrument tip localization for neurosurgical microscope data, formulated as coarse saliency prediction. For our analysis, we build a comprehensive dataset comprising in-the-wild data from several neurosurgical sub-disciplines as well as phantom surgeries. Comparing single stream networks using either image or optical flow information, we find complementary performance of both networks. Plain optical flow enables better cross-domain generalization, while the image-based network performs better on surgeries from the training domain. Based on these findings, we present a two-stream architecture that fuses image and optical flow information to utilize the complementary performance of both. Being trained on tumor surgeries, our architecture outperforms both single stream networks and shows improved robustness on data from different neurosurgical sub-disciplines. From our findings, future work must focus more on how to incorporate optical flow information into fusion architectures to further improve cross-domain generalization.')
}}
{{ paper('Weakly Supervised Volumetric Segmentation via Self-taught Shape Denoising Model',
        'Qian He, Shuailin Li, Xuming He',
        openreview='https://openreview.net/forum?id=Koyg3kvH-Mq',
        pdf='/proceedings/he21.pdf',
        id='A8',
        paper='papers/A8.html',
        proceedings='',
        abstract='Weakly supervised segmentation is an important problem in medical image analysis due to the high cost of pixelwise annotation. Prior methods, while often focusing on weak labels of 2D images, exploit few structural cues of volumetric medical images. To address this, we propose a novel weakly-supervised segmentation strategy capable of better capturing 3D shape prior in both model prediction and learning. Our main idea is to extract a self-taught shape representation by leveraging weak labels, and then integrate this representation into segmentation prediction for shape refinement. To this end, we design a deep network consisting of a segmentation module and a shape denoising module, which are trained by an iterative learning strategy. Moreover, we introduce a weak annotation scheme with a hybrid label design for volumetric images, which improves model learning without increasing the overall annotation cost. The empirical experiments show that our approach outperforms existing SOTA strategies on three organ segmentation benchmarks with distinctive shape properties. Notably, we can achieve strong performance with even 10% labeled slices, which is significantly superior to other methods.')
}}
{{ paper('Benefits of Linear Conditioning for Segmentation using Metadata',
        'Andreanne Lemay, Charley Gros, Olivier Vincent, Yaou Liu, Joseph Paul Cohen, Julien Cohen-Adad',
        openreview='https://openreview.net/forum?id=fa176bQAbr',
        pdf='/proceedings/lemay21.pdf',
        id='A9',
        paper='papers/A9.html',
        proceedings='',
        abstract="Medical images are often accompanied by metadata describing the image (vendor, acquisition parameters) and the patient (disease type or severity, demographics, genomics). This metadata is usually disregarded by image segmentation methods. In this work, we adapt a linear conditioning method called FiLM (Feature-wise Linear Modulation) for image segmentation tasks. This FiLM adaptation enables integrating metadata into segmentation models for better performance. We observed an average Dice score increase of 5.1% on spinal cord tumor segmentation when incorporating the tumor type with FiLM. The metadata modulates the segmentation process through low-cost affine transformations applied on feature maps which can be included in any neural network\\'s architecture. Additionally, we assess the relevance of segmentation FiLM layers for tackling common challenges in medical imaging: training with limited or unbalanced number of annotated data, multi-class training with missing segmentations, and model adaptation to multiple tasks. Our results demonstrated the following benefits of FiLM for segmentation: FiLMed U-Net was robust to missing labels and reached higher Dice scores with few labels (up to 16.7%) compared to single-task U-Net. The code is open-source and available at www.ivadomed.org.")
}}
{{ paper('Distill DSM: Computationally efficient method for segmentation of medical imaging volumes',
        'Harsh Maheshwari, Vidit Goel, Ramanathan Sethuraman, Debdoot Sheet',
        openreview='https://openreview.net/forum?id=_n48l6YKc6d',
        pdf='/proceedings/maheshwari21.pdf',
        id='A10',
        paper='papers/A10.html',
        proceedings='',
        abstract='Accurate segmentation of volumetric scans like MRI and CT scans is highly demanded for surgery planning in clinical practice, quantitative analysis, and identification of disease. However, accurate segmentation is challenging because of the irregular shape of given organ and large variation in appearances across the slices. In such problems, 3D features are desired in nature which can be extracted using 3D convolutional neural network (CNN). However, 3D CNN is compute and memory intensive to implement due to large number of parameters and can easily over fit, especially in medical imaging where training data is limited. In order to address these problems, we propose a distillation-based depth shift module (Distill DSM). It is designed to enable 2D convolutions to make use of information from neighbouring frames more efficiently. Specifically, in each layer of the network, Distill DSM learns to extract information from a part of the channels and shares it with neighbouring slices, thus facilitating information exchange among neighbouring slices. This approach can be incorporated with any 2D CNN model to enable it to use information across the slices with introducing very few extra learn-able parameters. We have evaluated our model on BRATS 2020, heart, hippocampus, pancreas and prostate dataset. Our model achieves better performance than 3D CNN for heart and prostate datasets and comparable performance on BRATS 2020, pancreas and hippocampus dataset with simply 28\\% of parameters compared to 3D CNN model. ')
}}
{{ paper('Stroke Lesion Outcome Prediction Based on 4D CT Perfusion Data Using Temporal Convolutional Networks',
        'Kimberly Amador, Matthias Wilms, Anthony Winder, Jens Fiehler, Nils Forkert',
        openreview='https://openreview.net/forum?id=0YDEgvfwEW',
        pdf='/proceedings/amador21.pdf',
        id='A11',
        paper='papers/A11.html',
        proceedings='',
        abstract='Acute ischemic stroke is caused by a blockage in the cerebral arteries, resulting in long-term disability and sometimes death. To determine the optimal treatment strategy, a patient-specific assessment is often based on advanced neuroimaging data, such as spatio-temporal (4D) CT Perfusion (CTP) imaging. To date, perfusion maps are typically calculated from 4D CTP data and then thresholded to localize and quantify the stroke lesion core and tissue-at-risk. A few studies have recently developed deep learning methods to predict stroke lesion outcomes from perfusion maps. The basic idea of these is to train a model, using perfusion maps acquired at baseline and their corresponding follow-up images acquired several days after treatment, to automatically estimate the final lesion location and volume in new patients. Nevertheless, model training based on the original 4D CTP scans might be desirable, as they could contain more valuable information not directly represented in perfusion maps. Therefore, we aimed to develop and evaluate a temporal convolutional neural network (TCN) to predict stroke lesion outcomes directly from 4D CTP datasets acquired at admission, without computing any perfusion maps. Using a total of 176 CTP scans, we investigated the impact of the time window size by training the proposed TCN on various numbers of CTP frames: 8, 16, and 32 time points. For comparison purposes, we also trained a convolutional neural network based on perfusion maps. The results show that the model trained on 32 time points yielded significantly higher Dice values (0.33 +/- 0.21) than the models trained on 8 time points (0.25 +/- 0.20; P<0.05), 16 time points (0.28 +/- 0.21; P<0.001), and perfusion maps (0.23 +/- 0.18; P<0.05). These experiments demonstrate that the proposed model effectively extracts spatio-temporal data from CTP scans to predict stroke lesion outcomes, which leads to better results than using perfusion maps. ')
}}
{{ paper('Direct Inference of Cell Positions using Lens-Free Microscopy and Deep Learning',
        'Philipp Gruening, Falk Nette, Noah Heldt, Ana Cristina Guerra de Souza, Erhardt Barth',
        openreview='https://openreview.net/forum?id=2fpsTsvCgc0',
        pdf='/proceedings/gruening21.pdf',
        id='A12',
        paper='papers/A12.html',
        proceedings='',
        abstract='With in-line holography, it is possible to record biological cells over time in a three-dimensional hydrogel without the need for staining, providing the capability of observing cell behavior in a minimally invasive manner. However, this setup currently requires computationally intensive image-reconstruction algorithms to determine the required cell statistics. In this work, we directly extract cell positions from the holographic data by using deep neural networks and thus avoid several reconstruction steps. We show that our method is capable of substantially decreasing the time needed to extract information from the raw data without loss in quality.')
}}
[% / %]
<a id="shortB"></a><h3>B1-9 (short): Application: Histopathology - 13:45 - 14:30 (UTC+2)</h3>
Chairs: Mitko Veta, Jianhua Yao <br>
[% .papers %]
{{ paper('μPEN: Multi-class PseudoEdgeNet for PD-L1 assessment',
        'Jeroen Vermazeren, Leander van Eekelen, Luca Dulce Meesters, Monika Looijen-Salamon, Shoko Vos, Enrico Munari, Caner Mercan, Francesco Ciompi',
        openreview='https://openreview.net/forum?id=rHAiz2pnxkB',
        pdf='https://openreview.net/pdf?id=rHAiz2pnxkB',
        id='B1',
        paper='papers/B1.html',
        proceedings='',
        abstract='In this paper, we take the recently presented PseudoEdgeNet model to the level of multi-class cell segmentation in histopathology images solely trained with point annotations. We tailor its loss function to the challenges of multi-class segmentation and equip it with an additional false positive loss term. We evaluate it on the assessment of tumor and immune cells in PD-L1 stained lung cancer histopathology images, and compare it with YOLOv5.')
}}
{{ paper('Comparison of CNN models on a multi-scanner database in colon cancer histology',
        'Petr Kuritcyn, Michaela Benz, Jakob Dexl, Volker Bruns, Arndt Hartmann, Carol Geppert',
        openreview='https://openreview.net/forum?id=CdQn5goh0E4',
        pdf='https://openreview.net/pdf?id=CdQn5goh0E4',
        id='B2',
        paper='papers/B2.html',
        proceedings='',
        abstract='One of the most important challenges for computer-aided analysis in digital pathology is the development of robust deep neural networks, which can cope with variations in color and resolution of digitized whole-slide images (WSIs). It has been shown that color augmentation during training is a useful method to aid a model generalize better to heterogeneous data. In this work, we compare state of the art models EfficientNet, Xception, Inception, ResNet, DenseNet, MobileNet and QuickNet on a multi-scanner database comprising slides each digitized with six different scanners. All of the networks are trained with data of only one scanner applying a combination of color and blur augmentation techniques. All models show similar tendencies across the different scanner databases but differ in the overall classification accuracy. Differences in training and inference time, however, are more pronounced: on a mid-range GPU, the inference time of the fastest model (QuickNet) is 13 times faster than the slowest one (EfficientNet B4). There is also a trade-off between speed and accuracy, the slower networks are more stable across different scanners and show the overall best performance. A good compromise between quality and inference time is achieved by EfficientNet B0.')
}}
{{ paper('Exploiting Adam-like Optimization Algorithms to Improve the Performance of Convolutional Neural Networks',
        'Loris Nanni, Gianluca Maguolo, Alessandra Lumini',
        openreview='https://openreview.net/forum?id=RFwhfWEMyzm',
        pdf='https://openreview.net/pdf?id=RFwhfWEMyzm',
        id='B3',
        paper='papers/B3.html',
        proceedings='',
        abstract='Stochastic gradient descent (SGD) is the main approach for training deep networks: it moves towards the optimum of the cost function by  iteratively updating the parameters of a model in the direction of the gradient of the loss evaluated on a minibatch. Several variants of SGD have been proposed to make adaptive step sizes for each parameter (adaptive gradient) and take into account the previous updates (momentum). Among several alternative of SGD the most popular are AdaGrad, AdaDelta, RMSProp and Adam which scale coordinates of the gradient by square roots of some form of averaging of the squared coordinates in the past gradients and automatically adjust the learning rate on a parameter basis. In this work, we compare Adam based variants based on the difference between the present and the past gradients, the step size is adjusted for each parameter. We run several tests benchmarking proposed methods using medical image data. The experiments are performed using ResNet50 architecture neural network. Moreover, we have tested ensemble of networks and the fusion with ResNet50 trained with stochastic gradient descent. To combine the set of ResNet50 the simple sum rule has been applied. Proposed ensemble obtains very high performance, it obtains accuracy comparable or better than actual state of the art. To improve reproducibility and research efficiency the MATLAB source code used for this research is available at GitHub: https://github.com/LorisNanni.')
}}
{{ paper('Gated CNNs for Nuclei Segmentation in H&E Breast Images',
        'Shana Beniamin, April Khademi, Dimitri Androutsos',
        openreview='https://openreview.net/forum?id=fQDGt0RJkMu',
        pdf='https://openreview.net/pdf?id=fQDGt0RJkMu',
        id='B4',
        paper='papers/B4.html',
        proceedings='',
        abstract='Nuclei segmentation using deep learning has been achieving high accuracy using U-Net and variants, but a remaining challenge is distinguishing touching and overlapping cells. In this work, we propose using gated CNN (GCNN) networks to obtain sharper predictions around object boundaries and improve nuclei segmentation performance. The method is evaluated in over 1000 multicentre diverse H&E breast cancer images from three databases and compared to baseline U-Net and R2U-Net.')
}}
{{ paper('Strength in Diversity: Understanding the impacts of diverse training sets in self-supervised pre-training for histology images',
        'Kristina Lynn Kupferschmidt, Eu Wern Teh, Graham W. Taylor',
        openreview='https://openreview.net/forum?id=cA4VVWbNO-',
        pdf='https://openreview.net/pdf?id=cA4VVWbNO-',
        id='B5',
        paper='papers/B5.html',
        proceedings='',
        abstract='Self-supervised learning (SSL) has demonstrated success in computer vision tasks for natural images, and recently histopathological images, where there is limited availability of annotations. Despite this, there has been limited research into how the diversity of source data used for SSL tasks impacts performance. The current study quantifies changes to downstream classification of metastatic tissue in lymph node sections of the PatchCamelyon dataset when datasets from different domains (natural images, textures, histology) are used for SSL pre-training. We show that for cases with limited training data, using diverse datasets from different domains for SSL pre-training can achieve comparable performance when compared with SSL pre-training on the target dataset.')
}}
{{ paper('Abnormality Detection in Histopathology via Density Estimation with Normalising Flows',
        'Nick Pawlowski, Ben Glocker',
        openreview='https://openreview.net/forum?id=-j7vnPsPWys',
        pdf='https://openreview.net/pdf?id=-j7vnPsPWys',
        id='B6',
        paper='papers/B6.html',
        proceedings='',
        abstract='Diagnosis of cancer often relies on the time-consuming examination of histopathology slides by expert pathologists. Automation via supervised deep learning methods require large amounts of pixel-wise annotated data that is costly to acquire. Unsupervised density estimation methods that rely only on the availability of healthy examples could cut down the cost of annotation. We propose to use residual flows as density estimator and compare different tests for out-of-distribution (OOD) detection. Our results suggest that unsupervised OOD detection is a viable approach for detecting suspicious regions in histopathology slides.')
}}
{{ paper('Learning to Represent Whole Slide Images by Selecting Cell Graphs of Patches',
        'Yinan Zhang, Beril Besbinar, Pascal Frossard',
        openreview='https://openreview.net/forum?id=hPUnpHJHuy',
        pdf='https://openreview.net/pdf?id=hPUnpHJHuy',
        id='B7',
        paper='papers/B7.html',
        proceedings='',
        abstract='Advances in multiplex biomarker imaging systems have enabled the study of complex spatial biology within the tumor microenvironment. However, the high-resolution multiplexed images are often only available for a subset of regions of interest (RoIs), clinical data is not easily accessible and the datasets are generally too small to apply off-the-shelf deep learning methods commonly used in histopathology. In this paper, we focus on datasets with few images and without labels, and aim to learn representations for slides. We choose a task of patient identification that leads our new model to select RoIs with discriminative properties and infer patient-specific features that can be used later for any task via transfer learning. The experimental results on the synthetic data generated by taking the tumor microenvironment into account indicate that the proposed method is a promising step towards computer-aided analysis in unlabeled datasets of high-resolution images.')
}}
{{ paper('Quality control of whole-slide images through multi-class semantic segmentation of artifacts',
        'Gijs Smit, Francesco Ciompi, Maria Cigéhn, Anna Bodén, Jeroen van der Laak, Caner Mercan',
        openreview='https://openreview.net/forum?id=7EZ4JOtlRl',
        pdf='https://openreview.net/pdf?id=7EZ4JOtlRl',
        id='B8',
        paper='papers/B8.html',
        proceedings='',
        abstract='Quality control is an integral part in the digitization process of whole-slide histopathology images due to artifacts that arise during various stages of slide preparation. Manual control and supervision of these gigapixel images are labor-intensive.  Therefore, we report the first multi-class deep learning model trained on whole-slide images covering multiple tissue and stain types for semantic segmentation of artifacts.  Our approach reaches a Dice score of 0.91, on average, across six artifact types, and outperforms the competition on external test set. Finally, we extend the artifact segmentation network to a multi-decision quality control system that can be deployed in routine clinical practice.')
}}
{{ paper('Cluster-to-Conquer: A Framework for End-to-End Multi-Instance Learning for Whole Slide Image Classification',
        'Yash Sharma, Aman Shrivastava, Lubaina Ehsan, Christopher A. Moskaluk, Sana Syed, Donald Brown',
        openreview='https://openreview.net/forum?id=7i1-2oKIELU',
        pdf='/proceedings/sharma21.pdf',
        id='B9',
        paper='papers/B9.html',
        proceedings='',
        abstract="In recent years, the availability of digitized Whole Slide Images (WSIs) has enabled the use of deep learning-based computer vision techniques for automated disease diagnosis. However, WSIs present unique computational and algorithmic challenges. WSIs are gigapixel-sized (approx. 100K pixels), making them infeasible to be used directly for training deep neural networks. Also, often only slide-level labels are available for training as detailed annotations are tedious and can be time-consuming for experts. Approaches using multiple-instance learning (MIL) frameworks have been shown to overcome these challenges. Current state-of-the-art approaches divide the learning framework into two decoupled parts: a convolutional neural network (CNN) for encoding the patches followed by an independent aggregation approach for slide-level prediction. In this approach, the aggregation step has no bearing on the representations learned by the CNN encoder. We have proposed an end-to-end framework that clusters the patches from a WSI into k-groups, samples k\\' patches from each group for training, and uses an adaptive attention mechanism for slide level prediction; Cluster-to-Conquer (C2C). We have demonstrated that dividing a WSI into clusters can improve the model training by exposing it to diverse discriminative features extracted from the patches. We regularized the clustering mechanism by introducing a KL-divergence loss between the attention weights of patches in a cluster and the uniform distribution. The framework is optimized end-to-end on slide-level cross-entropy, patch-level cross-entropy, and KL-divergence loss.")
}}
[% / %]
<a id="longD"></a><h3>D1-3 (long): Unsupervised and Representation Learning - 16:00 - 16:30 (UTC+2)</h3>
Chairs: Jannis Hagenah, Caroline Petitjean <br>
[% .papers %]
{{ paper('Self-Rule to Adapt: Learning Generalized Features from Sparsely-Labeled Data Using Unsupervised Domain Adaptation for Colorectal Cancer Tissue Phenotyping',
        'Christian Abbet, Linda Studer, Andreas Fischer, Heather Dawson, Inti Zlobec, Behzad Bozorgtabar, Jean-Philippe Thiran',
        openreview='https://openreview.net/forum?id=VO7asaS5GUk',
        pdf='/proceedings/abbet21.pdf',
        id='D1',
        paper='papers/D1.html',
        proceedings='',
        abstract='Supervised learning is conditioned by the availability of labeled data, which are especially expensive to acquire in the field of medical image analysis. Making use of open-source data for pre-training or using domain adaptation can be a way to overcome this issue. However, pre-trained networks often fail to generalize to new test domains that are not distributed identically due to variations in tissue stainings, types, and textures. Additionally, current domain adaptation methods mainly rely on fully-labeled source datasets. In this work, we propose Self-Rule to Adapt (SRA) which takes advantage of self-supervised learning to perform domain adaptation and removes the burden of fully-labeled source datasets. SRA can effectively transfer the discriminative knowledge obtained from a few labeled source domain to a new target domain without requiring additional tissue annotations. Our method harnesses both domains’ structures by capturing visual similarity with intra-domain and cross-domain self-supervision. We show that our proposed method outperforms baselines across diverse domain adaptation settings and further validate our approach to our in-house clinical cohort.')
}}
{{ paper('Semantic similarity metrics for learned image registration',
        'Steffen Czolbe, Oswin Krause, Aasa Feragen',
        openreview='https://openreview.net/forum?id=9M5cH--UdcC',
        pdf='/proceedings/czolbe21.pdf',
        id='D2',
        paper='papers/D2.html',
        proceedings='',
        abstract='We propose a semantic similarity metric for image registration. Existing metrics like euclidean distance or normalized cross-correlation focus on aligning intensity values, giving difficulties with low intensity contrast or noise. Our approach learns dataset-specific features that drive the optimization of a learning-based registration model. We train both an unsupervised approach using an auto-encoder, and a semi-supervised approach using supplemental segmentation data to extract semantic features for image registration. Comparing to existing methods across multiple image modalities and applications, we achieve consistently high registration accuracy. A learned invariance to noise gives smoother transformations on low-quality images.')
}}
{{ paper('Nuc2Vec: Learning Representations of Nuclei in Histopathology Images with Contrastive Loss',
        'Chao Feng, Chad Vanderbilt, Thomas Fuchs',
        openreview='https://openreview.net/forum?id=uLtYvtWw8PH',
        pdf='/proceedings/feng21.pdf',
        id='D3',
        paper='papers/D3.html',
        proceedings='',
        abstract='The tumor microenvironment is an area of intense interest in cancer research and may be a clinically actionable aspect of cancer care. One way to study the tumor microenvironment is to characterize the spatial interactions between various types of nuclei in cancer tissue from H&E whole slide images, which require nucleus segmentation and classification. Current methods of nucleus classification rely on extensive labeling from pathologists and are limited by the number of categories a nucleus can be classified into. In this work, leveraging existing nucleus segmentation and contrastive representation learning methods, we developed a method that learns vector embeddings of nuclei based on their morphology in histopathology images. We show that the embeddings learned by this model capture distinctive morphological features of nuclei and can be used to group them into meaningful subtypes. These embeddings can provide a much richer characterization of the statistics of the spatial distribution of nuclei in cancer and open new possibilities in the quantitative study of the tumor microenvironment.')
}}
[% / %]
<a id="shortC"></a><h3>C1-9 (short): Endoscopy and Validation Studies - 16:45 - 17:30 (UTC+2)</h3>
Chairs: Sandy Engelhardt, Lena Maier-Hein <br>
[% .papers %]
{{ paper('Efficient biomedical image segmentation on Edge TPUs',
        'Andreas M Kist, Michael Döllinger',
        openreview='https://openreview.net/forum?id=HajxTQpPniD',
        pdf='https://openreview.net/pdf?id=HajxTQpPniD',
        id='C1',
        paper='papers/C1.html',
        proceedings='',
        abstract='Biomedical semantic segmentation is typically performed on dedicated, costly hardware. In a recent study, we suggested an optimized, tiny-weight U-Net for an inexpensive hardware accelerator, the Google Edge TPU. Using an open biomedical dataset for high-speed laryngeal videoendoscopy, we exemplarily show that we can dramatically reduce the parameter space and computations while keeping a high segmentation quality. Using a custom upsampling routine, we fully deployed optimized architectures to the Edge TPU. Combining the optimized architecture and the Edge TPU, we gain a total speedup of >79x compared to our initial baseline while keeping a high accuracy. This combination allows to provide immediate results at the point of care, especially in constrained computational environments.')
}}
{{ paper('Deep ensembles based on Stochastic Activation Selection for Polyp Segmentation',
        'Alessandra Lumini, Loris Nanni, Gianluca Maguolo',
        openreview='https://openreview.net/forum?id=NJcszyl19PN',
        pdf='https://openreview.net/pdf?id=NJcszyl19PN',
        id='C2',
        paper='papers/C2.html',
        proceedings='',
        abstract='Semantic segmentation has a wide array of applications ranging from medical-image analysis, scene understanding,\xa0autonomous driving and robotic navigation. This work deals with medical image segmentation and in particular with accurate polyp detection and segmentation during colonoscopy examinations. Several convolutional neural network architectures have been proposed to effectively deal with this task and with the problem of segmenting objects at different scale input. The basic architecture in image segmentation consists of an encoder and a decoder: the first uses convolutional filters to extract features from the image, the second is responsible for generating the final output. In this work, we compare some variant of the DeepLab architecture obtained by varying the decoder backbone. We compare several decoder architectures, including ResNet, Xception, EfficentNet, MobileNet and we perturb their layers by substituting ReLU activation layers with other functions. The resulting methods are used to create deep ensembles which are shown to be very effective. Our experimental evaluations show that our best ensemble produces good segmentation results by achieving high evaluation scores with a dice coefficient of  0.884, and a mean Intersection over Union (mIoU) of 0.818 for the Kvasir-SEG dataset. To improve reproducibility and research efficiency the MATLAB source code used for this research is available at GitHub: https://github.com/LorisNanni.')
}}
{{ paper('Self-supervised Visual Place Recognition for Colonoscopy Sequences',
        'Javier Morlana, Pablo Azagra Millán, Javier Civera, José M. M. Montiel',
        openreview='https://openreview.net/forum?id=tgkEqYyA12p',
        pdf='https://openreview.net/pdf?id=tgkEqYyA12p',
        id='C3',
        paper='papers/C3.html',
        proceedings='',
        abstract='We present the first place recognition system trained specifically for colonoscopy sequences. We use the convolutional neural network for image retrieval proposed by Radenovic et al. and we fine-tune it using image pairs from real human colonoscopies. The colonoscopy frames are clustered automatically by a Structure-from-Motion (SfM) algorithm, which has proven to cope with scene deformation and illumination changes. The experiments show that the system is able to generalize by testing in a different human colonoscopy, retrieving frames observing the same place despite of the different viewpoint and illumination changes. The proposed place recognition would be a key component of Simultaneous Localization and Mapping (SLAM) systems operating in colonoscopy to assist doctors during the explorations or to support robotization. ')
}}
{{ paper('Carbon footprint driven deep learning model selection for medical imaging',
        'Raghavendra Selvan',
        openreview='https://openreview.net/forum?id=1TPRpNyyj2L',
        pdf='https://openreview.net/pdf?id=1TPRpNyyj2L',
        id='C4',
        paper='papers/C4.html',
        proceedings='',
        abstract='Selecting task appropriate deep learning models is a resource intensive process; more so when working with large quantities of high dimensional data that are encountered in medical imaging. Model selection procedures that are primarily aimed at improving performance measures such as accuracy could become biased towards resource intensive models. In this work, we propose to inform and drive the model selection procedure using the carbon footprint of training deep learning models as a complementary measure along with other standard performance metrics. We experimentally demonstrate that increasing carbon footprint of large models might not necessarily translate into proportional performance gains, and suggest useful trade-offs to obtain resource efficient models.')
}}
{{ paper('SWNet: Surgical Workflow Recognition with Deep Convolutional Network',
        'Bokai Zhang, Amer Ghanem, Alexander Simes, Henry Choi, Andrew Yoo, Andrew Min',
        openreview='https://openreview.net/forum?id=g1sESqlP214',
        pdf='/proceedings/zhang21c.pdf',
        id='C5',
        paper='papers/C5.html',
        proceedings='',
        abstract='Surgical workflow recognition has been playing an essential role in computer-assisted interventional systems for modern operating rooms. In this paper, we present a computer vision-based method named SWNet that focuses on utilizing spatial information and temporal information from the surgical video to achieve surgical workflow recognition. As the first step, we utilize Interaction-Preserved Channel-Separated Convolutional Network (IP-CSN) to extract features that contain spatial information and local temporal information from the surgical video through segments. Secondly, we train a Multi-Stage Temporal Convolutional Network (MS-TCN) with those extracted features to capture global temporal information from the full surgical video. Finally, by utilizing Prior Knowledge Noise Filtering (PKNF), prediction noise from the output of MS-TCN is filtered. We evaluate SWNet for Sleeve Gastrectomy surgical workflow recognition. SWNet achieves 90% frame-level accuracy and reaches a weighted Jaccard Score of 0.8256. This demonstrates that SWNet has considerable potential to solve the surgical workflow recognition problem.')
}}
{{ paper('“Train one, Classify one, Teach one” - Cross-surgery transfer learning for surgical step recognition',
        'Daniel Neimark, Omri Bar, Maya Zohar, Gregory D. Hager, Dotan Asselmann',
        openreview='https://openreview.net/forum?id=cTB4Qz3RzCl',
        pdf='/proceedings/neimark21.pdf',
        id='C6',
        paper='papers/C6.html',
        proceedings='',
        abstract='Prior work demonstrated the ability of machine learning to automatically recognize surgical workflow steps from videos. However, these studies focused on only a single type of procedure. In this work, we analyze, for the first time, surgical step recognition on four different laparoscopic surgeries: Cholecystectomy, Right Hemicolectomy, Sleeve Gastrectomy, and Appendectomy. Inspired by the traditional apprenticeship model, in which surgical training is based on the Halstedian method, we paraphrase the “see one, do one, teach one” approach for the surgical intelligence domain as “train one, classify one, teach one”. In machine learning, this approach is often referred to as transfer learning. To analyze the impact of transfer learning across different laparoscopic procedures, we explore various time-series architectures and examine their performance on each target domain. We introduce a new architecture, the Time-Series Adaptation Network (TSAN), an architecture optimized for transfer learning of surgical step recognition, and we show how TSAN can be pre-trained using self-supervised learning on a Sequence Sorting task. Such pre-training enables TSAN to learn workflow steps of a new laparoscopic procedure type from only a small number of labeled samples from the target procedure. Our proposed architecture leads to better performance compared to other possible architectures, reaching over 90% accuracy when transferring from laparoscopic Cholecystectomy to the other three procedure types. ')
}}
{{ paper('Predicting COVID-19 Lung Infiltrate Progression on Chest Radiographs Using Spatio-temporal LSTM based Encoder-Decoder Network',
        'Aishik Konwer, Joseph Bae, Gagandeep Singh, Rishabh Gattu, Syed Ali, Jeremy Green, Tej Phatak, Amit Gupta, Chao Chen, Joel Saltz, Prateek Prasanna',
        openreview='https://openreview.net/forum?id=96BhL_MERil',
        pdf='/proceedings/konwer21.pdf',
        id='C7',
        paper='papers/C7.html',
        proceedings='',
        abstract='Automated analyses of chest imaging in Coronavirus Disease 2019 (COVID-19) have largely focused on a single timepoint, usually at disease presentation, and have not explicitly taken into account temporal disease manifestations. We present a deep learning-based approach for prediction of imaging progression from serial chest radiographs (CXRs) of COVID-19 patients. Our method first utilizes convolutional neural networks (CNNs) for feature extraction from patches within the concerned lung zone, and also from neighboring areas to enhance the contextual phenotypic information. The framework further incorporates two distinct spatio-temporal Long Short Term Memory (LSTM) modules for effective predictions. The first LSTM module captures spatial dependencies between patches and the second exploits the temporal context of sequential CXR scans. The resulting network focuses on critical image regions that provide relevant information for learning the progression of lung infiltrates without the explicit need for infiltrate segmentation. The second LSTM provides an encoded context vector used as an input to a decoder module to predict future severity grades. Our novel multi-institutional dataset comprises sequential CXR scans from N=100 patients. Specifically, our framework predicts zone-wise disease severity for a patient on the last day by learning representations from the previous temporal CXRs. We design two baseline approaches - one using fine-tuned VGG-16 features and the other using radiomic descriptors. Experimental results demonstrate that our proposed approach outperforms both baselines in average accuracy by 10.33% and 12.16%, respectively, in predicting COVID-19 progression severity.')
}}
{{ paper('Feature-based image registration in structured light endoscopy',
        'Andreas M Kist, Julian Zilker, Michael Döllinger, Marion Semmler',
        openreview='https://openreview.net/forum?id=MzC8X6cMF2r',
        pdf='/proceedings/kist21.pdf',
        id='C8',
        paper='papers/C8.html',
        proceedings='',
        abstract='Images offer a two-dimensional (2D) representation of a three-dimensional (3D) environment. However, in many biomedical tasks, a 3D view is crucial for diagnosis. Projecting structured light, such as a regular laser grid, onto the surface of interest allows to reconstruct its 3D structure. For reconstruction, it is crucial to correctly identify and assign each laser ray to its respective position in the laser grid. Current methods for this task use semi-automatic, yet highly manual annotations. Hence, a fully automatic, reliable method is desired. Here, we show that this assignment can be approached as an image registration. We first separate the laser rays from the background using semantic segmentation. We found that registration of the extracted laser rays directly to the fixed laser grid image fails, when we use state-of-the-art intensity-based image registration techniques, such as ANTs. Using our feature-based custom loss and a deep neural network, we are able to use a U-Net-like architecture to compute deformation fields to successfully register the laser rays onto the fixed image accompanied with a custom post-processing sorting step. Using synthetic data, we show that the network is in general able to learn affine and non-linear transformations. Our method is also robust to missing or occluded rays. Using an ex vivo dataset, we achieved an registration accuracy of 91%. In summary, we provide a new platform to perform feature-based registration and showcase this on a biomedical dataset. In future, we will evaluate different architectural designs and more complex datasets. ')
}}
{{ paper('Intensity Correction and Standardization for Electron Microscopy Data',
        'Oleh Dzyubachyk, Roman I Koning, Aat A Mulder, M. Christina Avramut, Frank GA Faas, Abraham J Koster',
        openreview='https://openreview.net/forum?id=MAUkVcDzDPA',
        pdf='/proceedings/dzyubachyk21.pdf',
        id='C9',
        paper='papers/C9.html',
        proceedings='',
        abstract='Intensity of acquired electron microscopy data is subjected to large variability due to the interplay of many different factors, such as microscope and camera settings used for data acquisition, sample thickness, specimen staining protocol and more. In this work, we developed an efficient method for performing intensity inhomogeneity correction on a single set of combined transmission electron microscopy (TEM) images and demonstrated its positive impact on training a neural network on these data. In addition, we investigated what impact different intensity standardization methods have on the training performance, both for data originating from a single source as well as from several different sources. As a concrete example, we considered the problem of segmenting mitochondria from EM data and demonstrated that we were able to obtain promising results when training our network on a large array of highly-variable in-house TEM data.')
}}
[% / %]
<a id="shortD"></a><h3>D4-12 (short): Detection and Diagnosis 1 - 16:45 - 17:30 (UTC+2)</h3>
Chairs: Tal Arbel, Hans Meine <br>
[% .papers %]
{{ paper('Predicting molecular subtypes of breast cancer using multimodal deep learning and incorporation of the attention mechanism',
        'Tianyu Zhang, Luyi Han, Yuan Gao, Xin Wang, Regina Beets-Tan, Ritse Mann',
        openreview='https://openreview.net/forum?id=GHNGMR1EAtN',
        pdf='https://openreview.net/pdf?id=GHNGMR1EAtN',
        id='D4',
        paper='papers/D4.html',
        proceedings='',
        abstract='Accurately determining the molecular subtype of breast cancer is an important factor for the prognosis of breast cancer patients, and can guide treatment selection. In this study, we report a multimodal deep learning with attention mechanism (MDLA) for predicting the molecular subtypes of breast cancer from mammography and ultrasound images. Incorporation of the attention mechanism improved diagnostic performance for predicting 4-class molecular subtypes with Matthews correlation coefficient (MCC) of 0.794. The MDLA can also discriminate between Luminal disease and non-luminal disease with areas under the receiver operating characteristic curve (AUC) of 0.855. This work thus provides a noninvasive imaging biomarker to predict the molecular subtypes of breast cancer.')
}}
{{ paper('Double adversarial domain adaptation for whole-slide-imageclassification',
        'Yuchen Yang, Amir Akbarnejad, Nilanjan Ray, Gilbert Bigras',
        openreview='https://openreview.net/forum?id=70gFxx5ytwh',
        pdf='https://openreview.net/pdf?id=70gFxx5ytwh',
        id='D5',
        paper='papers/D5.html',
        proceedings='',
        abstract='Image classification on whole-slide-image (WSI) is a challenging task. A previous work based on Fisher vector encoding provided a novel end-to-end pipeline with promising accuracy and computational efficiency.However, this pipeline suffers from an accuracy drop when deployed to another dataset to perform the same task.This poses a limitation on the practical use of the pipeline especially when the diagnoses of WSIs are hard to obtain.This paper aims at providing a solution to mitigate the accuracy drop by using an unsupervised domain adaptation approach.We propose to insert the domain classifiers into the pipeline in two stages to align the features during training. We evaluate accuracy by calculating the confusion matrices before and after the adaptation on two datasets. We demonstrate that placing domain classifiers in different stages will boost accuracy.')
}}
{{ paper('Virtual Bone Shape Aging',
        'Francesco Caliva, Alejandro Morales Martinez, Sharmila Majumdar, Valentina Pedoia',
        openreview='https://openreview.net/forum?id=1JP1g5htY6K',
        pdf='https://openreview.net/pdf?id=1JP1g5htY6K',
        id='D6',
        paper='papers/D6.html',
        proceedings='',
        abstract='We use deep learning to age knee bone surfaces four years. We propose to encode an MRI-based bone surface in a spherical coordinate format, and use these spherical maps to predict shape changes in a 48 months time frame, in subjects with and without osteoarthritis. The experiments show that a 2D V-Net can predict bone surface shape with a mean absolute error of about 1 mm. Our code is available  at https://github.com/fcaliva/Bone_Shape_Virtual_Aging.')
}}
{{ paper('Breast cancer patient stratification using domain adaptation based lymphocyte detection in HER2 stained tissue sections',
        'Ansh Kapil, Armin Meier, Anatoliy Shumilov, Susanne Haneder, Helen Angell, Günter Schmidt',
        openreview='https://openreview.net/forum?id=IAuBCvaTKHr',
        pdf='https://openreview.net/pdf?id=IAuBCvaTKHr',
        id='D7',
        paper='papers/D7.html',
        proceedings='',
        abstract='We extend the CycleGAN architecture with a style-based generator and show the efficacy of the proposed domain adaptation-based method between two histopathology image domains - Hematoxylin and Eosin (H&E) and HER2 immunohistochemically (IHC) images. Using the proposed method, we re-used large set of pre-existing annotations for detection of tumor infiltrating lymphocytes (TILs), which were originally done on H&E, towards a TIL detector applicable on HER2 IHC images. We provide analytical validation of the resulting TIL detector. Furthermore, we show that the detected stromal TIL densities are significantly prognostic as a biomarker for patient stratification on a triple-negative breast cancer (TNBC) cohort.')
}}
{{ paper('Cine-MRI detection of abdominal adhesions with spatio-temporal deep learning',
        'Bram de Wilde, Richard P. G. ten Broek, Henkjan Huisman',
        openreview='https://openreview.net/forum?id=-KI5qmKvhKQ',
        pdf='https://openreview.net/pdf?id=-KI5qmKvhKQ',
        id='D8',
        paper='papers/D8.html',
        proceedings='',
        abstract='Adhesions are an important cause of chronic pain following abdominal surgery. Recent developments in abdominal cine-MRI have enabled the non-invasive diagnosis of adhesions. Adhesions are identified on cine-MRI by the absence of sliding motion during movement. Diagnosis and mapping of adhesions  improves the management of patients with pain. Detection of abdominal adhesions on cine-MRI is challenging from both a radiological and deep learning perspective. We focus on classifying presence or absence of adhesions in sagittal abdominal cine-MRI series. We experimented with spatio-temporal deep learning architectures centered around a ConvGRU architecture. A hybrid architecture comprising a ResNet followed by a ConvGRU model allows to classify a whole time-series. Compared to a stand-alone ResNet with a two time-point (inspiration/expiration) input, we show an increase in classification performance (AUROC) from 0.74 to 0.83 (p<0.05). Our full temporal classification approach adds only a small amount (5%) of parameters to the entire architecture, which may be useful for other  medical imaging problems with a temporal dimension. ')
}}
{{ paper('Efficient Video-Based Deep Learning for Ultrasound Guided Needle Insertion',
        'Jonathan Rubin, Alvin Chen, Anumod Odungattu Thodiyil, Raghavendra Srinivasa Naidu, Ramon Erkamp, Jon Fincke, Balasundar Raju',
        openreview='https://openreview.net/forum?id=dVUHL5QhDhL',
        pdf='https://openreview.net/pdf?id=dVUHL5QhDhL',
        id='D9',
        paper='papers/D9.html',
        proceedings='',
        abstract='We investigate video-based deep learning approaches for detecting needle insertions in ultrasound videos. We introduce two efficient and conceptually simple extensions to convert standard 2D object detectors into video object detectors that make use of temporal information from a history of frames. We compare our approaches to a 2D baseline method that makes independent predictions per frame. Given the need to run in real-time on computationally restricted environments, emphasis is placed on low computational complexity.')
}}
{{ paper('An AI-based Framework for Diagnostic Quality Assessment of Ankle Radiographs',
        'Dominik Mairhöfer, Manuel Laufer, Paul Martin Simon, Malte Sieren, Arpad Bischof, Thomas Käster, Erhardt Barth, Jörg Barkhausen, Thomas Martinetz',
        openreview='https://openreview.net/forum?id=bj04hJss_xZ',
        pdf='/proceedings/mairhoefer21.pdf',
        id='D10',
        paper='papers/D10.html',
        proceedings='',
        abstract='The quality of radiographs is of major importance for diagnosis and treatment planning. While most research regarding automated radiograph quality assessment uses technical features such as noise or contrast, we propose to use anatomical structures as more appropriate features. We show that based on such anatomical features, a modular deep-learning framework can serve as a quality control mechanism for the diagnostic quality of ankle radiographs. For evaluation, a dataset consisting of 950 ankle radiographs was collected and their quality was labeled by radiologists. We obtain an average accuracy of 94.1%, which is better than the expert radiologists are on average.')
}}
{{ paper('Image Sequence Generation and Analysis via GRU and Attention for Trachomatous Trichiasis Classification',
        'Juan Carlos Prieto, Hina Shah, Kasey Jones, Robert F Chew, Hashiya M. Kana, Jerusha Weaver, Rebecca M. Flueckiger, Scott McPherson, Emily W. Gower',
        openreview='https://openreview.net/forum?id=umb5xsy1-zS',
        pdf='/proceedings/prieto21.pdf',
        id='D11',
        paper='papers/D11.html',
        proceedings='',
        abstract='Chlamydia trachomatous is an infectious ocular condition that can cause the eyelid to turn inward so that one or more eyelashes touch the eyeball, a condition call trachomatous trichiasis (TT), which can lead to blindness. Community-based screeners are used in rural areas to identify patients with TT, who can then be referred for proper medical care. Having automatic methods to detect TT will reduce the amount of time required to train screeners and improve accuracy of detection. This paper proposes a method to automatically identify regions of an eye and identify TT, using photographs taken with smartphones in the field. The attention-based gated deep learning networks in combination with a regionidentification network can identify TT with an accuracy of 91%, sensitivity of 92% and specificity of 87%, showing that these methods have the potential to be deployed in the field.')
}}
{{ paper('MoCo Pretraining Improves Representation and Transferability of Chest X-ray Models',
        'Hari Sowrirajan, Jingbo Yang, Andrew Y. Ng, Pranav Rajpurkar',
        openreview='https://openreview.net/forum?id=LO7Su0-dPJl',
        pdf='/proceedings/sowrirajan21.pdf',
        id='D12',
        paper='papers/D12.html',
        proceedings='',
        abstract='Contrastive learning is a form of self-supervision that can leverage unlabeled data to produce pretrained models. While contrastive learning has demonstrated promising results on natural image classification tasks, its application to medical imaging tasks like chest X-ray interpretation has been limited. In this work, we propose MoCo-CXR, which is an adaptation of the contrastive learning method Momentum Contrast (MoCo), to produce models with better representations and initializations for the detection of pathologies in chest X-rays. In detecting pleural effusion, we find that linear models trained on MoCo-CXR-pretrained representations outperform those without MoCo-CXR-pretrained representations, indicating that MoCo-CXR-pretrained representations are of higher-quality. End-to-end fine-tuning experiments reveal that a model initialized via MoCo-CXR-pretraining outperforms its non-MoCo-CXR-pretrained counterpart. We find that MoCo-CXR-pretraining provides the most benefit with limited labeled training data. Finally, we demonstrate similar results on a target Tuberculosis dataset unseen during pretraining, indicating that MoCo-CXR-pretraining endows models with representations and transferability that can be applied across chest X-ray datasets and tasks.')
}}
[% / %]

<hr>

<h2> Thursday 8th July</h2>
<a id="longE"></a><h3>E1-3 (long): Detection and Diagnosis - 13:00 - 13:30 (UTC+2)</h3>
Chairs: Ivana Isgum, Carole Sudre <br>
[% .papers %]
{{ paper('Automated triaging of head MRI examinations using convolutional neural networks',
        'David A Wood, Sina Kafiabadi, Ayisha Al Busaidi, Emily Guilhem, Antanas Montvila, Siddharth Agarwal, Jeremy Lynch, Matthew Townend, Gareth Barker, Sebastien Ourselin, James H Cole, Thomas C Booth',
        openreview='https://openreview.net/forum?id=gh8qD_lAADe',
        pdf='/proceedings/wood21.pdf',
        id='E1',
        paper='papers/E1.html',
        proceedings='',
        abstract='The growing demand for head magnetic resonance imaging (MRI) examinations, along with a global shortage of radiologists, has led to an increase in the time taken to report head MRI scans around the world.  For many neurological conditions, this delay can result in increased morbidity and mortality.  An automated triaging tool could reduce reporting times for abnormal examinations by identifying abnormalities at the time of imaging and prioritizing the reporting of these scans.  In this work, we present a convolutional neural network (CNN) for detecting clinically-relevant  abnormalities  in T2-weighted  head  MRI scans. Using a validated neuroradiology report classifier, we generated a labelled dataset of 43,754 scans from two large UK hospitals for model training, and demonstrate accurate classification (area under the receiver operating curve (AUC) = 0.943) on a test set of 800 scans labelled by a team of neuroradiologists.  Importantly,  when trained on scans from only a single hospital the model generalized to scans from the other hospital (∆AUC≤0.02).  A simulation study demonstrated that our model would reduce the mean reporting time for abnormal scans from 28 days to 14 days and from 9 days to 5 days at the two hospitals, demonstrating feasibility for use in a clinical triage environment.')
}}
{{ paper('Balanced sampling for an object detection problem - application to fetal anatomies detection',
        'Antoine Olivier, Caroline Raynaud',
        openreview='https://openreview.net/forum?id=ZGvtypAfHiA',
        pdf='/proceedings/olivier21.pdf',
        id='E2',
        paper='papers/E2.html',
        proceedings='',
        abstract='In this paper, we propose a novel approach to overcome the problem of imbalanced datasets for object detection tasks, when the distribution is not uniform over all classes. The general idea is to compute a probability vector, encoding the probability for each image to be fed to the network during the training phase. This probability vector is computed by solving some quadratic optimization problem and ensures that all classes are seen with similar frequency. We apply this method to a fetal anatomies detection problem, and conduct a thorough statistical analysis of the resulting performance to show that it performs significantly better than two baseline models: one with images sampled uniformly and one implementing classical oversampling.')
}}
{{ paper('Unsupervised Brain Anomaly Detection and Segmentation with Transformers',
        'Walter Hugo Lopez Pinaya, Petru-Daniel Tudosiu, Robert Gray, Geraint Rees, Parashkev Nachev, Sébastien Ourselin, M. Jorge Cardoso',
        openreview='https://openreview.net/forum?id=Z1tlNqbCpp_',
        pdf='/proceedings/pinaya21.pdf',
        id='E3',
        paper='papers/E3.html',
        proceedings='',
        abstract='Pathological brain appearances may be so heterogeneous as to be intelligible only as anomalies, defined by their deviation from normality rather than any specific pathological characteristic. Amongst the hardest tasks in medical imaging, detecting such anomalies requires models of the normal brain that combine compactness with the expressivity of the complex, long-range interactions that characterise its structural organisation. These are requirements transformers have arguably greater potential to satisfy than other current candidate architectures, but their application has been inhibited by their demands on data and computational resource. Here we combine the latent representation of vector quantised variational autoencoders with an ensemble of autoregressive transformers to enable unsupervised anomaly detection and segmentation defined by deviation from healthy brain imaging data, achievable at low computational cost, within relative modest data regimes. We compare our method to current state-of-the-art approaches across a series of experiments involving synthetic and real pathological lesions. On real lesions, we train our models on 15,000 radiologically normal participants from UK Biobank, and evaluate performance on four different brain MR datasets with small vessel disease, demyelinating lesions, and tumours. We demonstrate superior anomaly detection performance both image-wise and pixel-wise, achievable without post-processing. These results draw attention to the potential of transformers in this most challenging of imaging tasks.')
}}
[% / %]
<a id="shortE"></a><h3>E4-12 (short): Image Registration / Synthesis - 13:45 - 14:30 (UTC+2)</h3>
Chairs: Alessa Hering, Hervé Lombaert <br>
[% .papers %]
{{ paper('Rethinking the Design of Learning based Inter-Patient Registration using Deformable Supervoxels ',
        'Mattias P Heinrich',
        openreview='https://openreview.net/forum?id=zZA5TpNdC4Z',
        pdf='https://openreview.net/pdf?id=zZA5TpNdC4Z',
        id='E4',
        paper='papers/E4.html',
        proceedings='',
        abstract='Deep learning has the potential to substantially improve inter-subject alignment for shape and atlas analysis. So far most highly accurate supervised approaches require dense manual annotations and complex multi-level architectures but may still be susceptible to label bias. We present a radically different approach for learning to estimate large deformations without expert supervision. Instead of regressing displacements, we train a 3D DeepLab network to predict automatic supervoxel segmentations. To enable consistent supervoxel labels, we use the warping field of a conventional approach and increase the accuracy by sampling multiple complementary over-segmentations. We experimentally demonstrate that 1) our deformable supervoxels are less sensitive to large initial misalignment and can combine linear and nonlinear registration and 2) using this self-supervised classification loss is more robust to noisy ground truth and leads to better convergence than direct regression as supervision.')
}}
{{ paper('Semi-supervised Image-to-Image translation for robust image registration',
        'henrik skibbe, akiya watakabe, Febrian Rachmadi, Carlos Enrique Gutierrez, Ken Nakae, tetsuo yamamori',
        openreview='https://openreview.net/forum?id=GOhAojdaLg',
        pdf='https://openreview.net/pdf?id=GOhAojdaLg',
        id='E5',
        paper='papers/E5.html',
        proceedings='',
        abstract='The Japan Brain/MINDS Project aims at studying the neural networks controlling higher brain functions in the marmoset. As part of it, we develop an image processing pipeline for marmoset brain imaging data, where various microscopy images of different modalities need to be co-registered. In initial experiments, multi-modal image registration frequently failed due to an erroneous initialization. Our data set includes images of Nissl stained brain sections, backlit images as well as images of neural tracer injections using two-photon microscopy. More than 10000 high-resolution 2D images required co-registration, a large amount that demands a reliable automation process. We implemented a semi-supervised image-to-image translation which allowed a robust image alignment initialization. With such an initial alignment, all images can be successfully registered using a state-of-the-art multi-modal image registration algorithm.')
}}
{{ paper('ViT-V-Net: Vision Transformer for Unsupervised Volumetric Medical Image Registration',
        'Junyu Chen, Yufan He, Eric Frey, Ye Li, Yong Du',
        openreview='https://openreview.net/forum?id=h3HC1EU7AEz',
        pdf='https://openreview.net/pdf?id=h3HC1EU7AEz',
        id='E6',
        paper='papers/E6.html',
        proceedings='',
        abstract='In the last decade, convolutional neural networks (ConvNets) have dominated and achieved state-of-the-art performances in a variety of medical imaging applications. However, the performances of ConvNets are still limited by lacking the understanding of long-range spatial relations in an image. The recently proposed Vision Transformer (ViT) for image classification uses a purely self-attention-based model that learns long-range spatial relations to focus on the relevant parts of an image. Nevertheless, ViT emphasizes the low-resolution features because of the consecutive downsamplings, result in a lack of detailed localization information, making it unsuitable for image registration. Recently, several ViT-based image segmentation methods have been combined with ConvNets to improve the recovery of detailed localization information. Inspired by them, we present ViT-V-Net, which bridges ViT and ConvNet to provide volumetric medical image registration. The experimental results presented here demonstrate that the proposed architecture achieves superior performance to several top-performing registration methods.')
}}
{{ paper('Learning a Metric without Supervision: Multimodal Registration using Synthetic Cycle Discrepancy',
        'Hanna Siebert, Lasse Hansen, Mattias P Heinrich',
        openreview='https://openreview.net/forum?id=sua3vlnkmEv',
        pdf='https://openreview.net/pdf?id=sua3vlnkmEv',
        id='E7',
        paper='papers/E7.html',
        proceedings='',
        abstract='Training deep learning based medical image registration methods involves the challenge of finding a suitable metric. To avoid the difficulty of choosing a metric for multimodal image registration, we propose a completely new concept relying on geometric instead of metric supervision with three-way registration cycles. Therefore, we create a synthetic image by applying a synthetic transformation on one of the input images. This leads to cycles that for each pair of input images comprise two multimodal transformations to be estimated and one known synthetic monomodal transformation. We minimise the discrepancy between the combined multimodal transformations and the synthetic monomodal transformation. By minimising this cycle discrepancy, we are able to learn multimodal registration between CT and MRI without metric supervision. Our method outperforms state-of-the-art metric supervision and comes very close to fully-supervised learning with ground truth labels. ')
}}
{{ paper('Learning Diffeomorphic and Modality-invariant Registration using B-splines',
        'Huaqi Qiu, Chen Qin, Andreas Schuh, Kerstin Hammernik, Daniel Rueckert',
        openreview='https://openreview.net/forum?id=eSI9Qh2DJhN',
        pdf='/proceedings/qiu21.pdf',
        id='E8',
        paper='papers/E8.html',
        proceedings='',
        abstract='We present a deep learning (DL) registration framework for fast mono-modal and multi-modal image registration using differentiable mutual information and diffeomorphic B-spline free-form deformation (FFD). Deep learning registration has been shown to achieve competitive accuracy and significant speedups from traditional iterative registration methods. In this paper, we propose to use a B-spline FFD parameterisation of Stationary Velocity Field (SVF) to in DL registration in order to achieve smooth diffeomorphic deformation while being computationally-efficient. In contrast to most DL registration methods which use intensity similarity metrics that assume linear intensity relationship, we apply a differentiable variant of a classic similarity metric, mutual information, to achieve robust mono-modal and multi-modal registration. We carefully evaluated our proposed framework on mono- and multi-modal registration using 3D brain MR images and 2D cardiac MR images.')
}}
{{ paper('A hybrid model- and deep learning-based framework for functional lung image synthesis from non-contrast multi-inflation CT',
        'Joshua Russell Astley, Alberto M Biancardi, Helen Marshall, Guilhem J Collier, Paul JC Hughes, Jim M Wild, Bilal A Tahir',
        openreview='https://openreview.net/forum?id=_BIpUlEB6ff',
        pdf='https://openreview.net/pdf?id=_BIpUlEB6ff',
        id='E9',
        paper='papers/E9.html',
        proceedings='',
        abstract='Hyperpolarized gas MRI can visualize and quantify regional lung ventilation with exquisite detail but requires highly specialized equipment and exogenous contrast. Alternative, non-contrast techniques, including CT-based models of ventilation have shown moderate spatial correlations with hyperpolarized gas MRI. Here, we propose a hybrid framework that integrates CT-ventilation modelling and deep learning approaches. The hybrid model/DL framework generated synthetic ventilation images which accurately replicated gross ventilation defects in hyperpolarized gas MRI scans, significantly outperforming other model- and DL-only approaches. Our results show that a synergy between conventional CT-ventilation modelling and DL can improve the performance of functional lung image synthesis.')
}}
{{ paper('Cycle Consistent Embedding of 3D Brains with Auto-Encoding Generative Adversarial Networks',
        'Shibo Xing, Harsh Sinha, Seong Jae Hwang',
        openreview='https://openreview.net/forum?id=jgBzGIG-kB',
        pdf='https://openreview.net/pdf?id=jgBzGIG-kB',
        id='E10',
        paper='papers/E10.html',
        proceedings='',
        abstract='Modern generative adversarial networks (GANs) have been enabling the realistic generation of full 3D brain images by sampling from a latent space prior Z (i.e., random vectors) and mapping it to realistic images in X (e.g., 3D MRIs). To address the ubiquitous mode collapse issue, recent works have strongly imposed certain characteristics such as Gaussianness to the prior by also explicitly mapping X to Z via encoder. These efforts, however, fail to accurately map 3D brain images to the desirable prior, which the generator assumes to be sampling the random vectors from. On the other hand, Variational Auto-Encoding GAN (VAE-GAN) solves mode collapse by enforcing Gaussianness by two learned parameter, yet causes blurriness in images. In this work, we show how our cycle consistent embedding} GAN (CCE-GAN) both accurately encodes 3D MRIs to the standard normal prior, and maintains the quality of the generated images. We achieve this without a network-based code discriminator via the Wasserstein measure. We quantitatively and qualitatively assess the embeddings and the generated 3D MRIs using healthy T1-weighted MRIs from ADNI.')
}}
{{ paper('Efficient and Accurate Spatial-Temporal Denoising Network for Low-dose CT Scans',
        'Leihao Wei, William Hsu',
        openreview='https://openreview.net/forum?id=XHWqF4DlRr0',
        pdf='https://openreview.net/pdf?id=XHWqF4DlRr0',
        id='E11',
        paper='papers/E11.html',
        proceedings='',
        abstract='While deep-learning-based imaging denoising techniques can improve the quality of low-dose computed tomography (CT) scans, repetitive 3D convolution operations cost significant computation resources and time. We present an efficient and accurate spatial-temporal convolution method to accelerate an existing denoising network based on the SRResNet. We trained and evaluated our model on our dataset containing 184 low-dose chest CT scans. We compared the performance of the proposed spatial-temporal convolution network to the SRResNet with full 3D convolutional layers. Using 8-bit quantization, we demonstrated a 7-fold speed-up during inference. Using lung nodule characterization as a driving task, we analyzed the impact on image quality and radiomic features. Our results show that our method achieves better perceptual quality, and the outputs are consistent with the SRResNet baseline outputs for some radiomics features (31 out of 57 total features). These observations together demonstrate that the proposed spatial-temporal method can be potentially useful for clinical applications where the computational resource is limited. ')
}}
{{ paper('Synthesis of Diabetic Retina Fundus Images Using Semantic Label Generation',
        'Joon-Ho Son, Amir Alansary, Daniel Rueckert, Bernhard Kainz, Benjamin Hou',
        openreview='https://openreview.net/forum?id=wiKDehhdnz',
        pdf='https://openreview.net/pdf?id=wiKDehhdnz',
        id='E12',
        paper='papers/E12.html',
        proceedings='',
        abstract='Automatic segmentation of retina lesions have been a long standing and challenging task for learning based models, mostly due to the lack of available and accurate lesion segmentation datasets. In this paper, we propose a two-step process for generating photo-realistic fundus images conditioned on synthetic \\"ground truth\\" semantic labels, and demonstrate its potential for further downstream tasks, such as, but not limited to; automated grading of diabetic retinopathy, dataset balancing, creating image examples for trainee ophthalmologists, etc.')
}}
[% / %]
<a id="shortF"></a><h3>F1-9 (short): Imaging: Reconstruction and Clinical Data - 13:45 - 14:30 (UTC+2)</h3>
Chairs: Nicha Dvornek, Bram van Ginneken <br>
[% .papers %]
{{ paper('Ex-vivo - to - In-vivo Learning in Cardiology',
        'Alexander M. Zolotarev, Oleg Y. Rogov, Aleksei V. Mikhailov, John D. Hummel, Vadim V Fedorov, Dmitry V. Dylov',
        openreview='https://openreview.net/forum?id=Tz_X8xpgYsO',
        pdf='https://openreview.net/pdf?id=Tz_X8xpgYsO',
        id='F1',
        paper='papers/F1.html',
        proceedings='',
        abstract='The clinical Atrial Fibrillation (AF) visualization method, multi-electrode mapping (MEM), delivers electrode grid in-vivo to the heart muscle and is known for its low resolution. A more cutting-edge imaging modality, near-infrared optical mapping (NIOM), allows seeing the AF sources in high resolution; however, it is currently ex-vivo only (i.e., designed for explanted organs only). In this work, we present the ex-vivo to the in-vivo learning paradigm, where the former serves the purpose of improving the latter. Specifically, the NIOM improves the detection of AF sources in MEM data via an image-to-image model. We validate the idea on 7 explanted human hearts and test the models on 2 clinical cases.')
}}
{{ paper('Reconstruction and coil combination of undersampled concentric-ring MRSI data using a Graph U-Net',
        'Paul Weiser, Stanislav Motyka, Georg Langs, Wolfgang Bogner',
        openreview='https://openreview.net/forum?id=vNPQTZfPjFO',
        pdf='https://openreview.net/pdf?id=vNPQTZfPjFO',
        id='F2',
        paper='papers/F2.html',
        proceedings='',
        abstract='Geometric deep learning has recently gained influence, as it allows the extension of convolutional neural networks to non euclidean domains. In this paper graph neural networks (GNNs) are used for reconstruction and coil combination of undersampled concentric-ring k-space MRSI data. We show that graph U-nets perform better on undersampled data than GNNs. Specifically, results suggest that the omission of self-connecting edges results in a more stable behavior and better training for graph U-nets.')
}}
{{ paper('ReconResNet: Regularised Residual Learning for MR Image Reconstruction of Undersampled Cartesian and Radial Data',
        'Soumick Chatterjee, Mario Breitkopf, Chompunuch Sarasaen, Hadya Yassin, Georg Rose, Andreas Nürnberger, Oliver Speck',
        openreview='https://openreview.net/forum?id=KNEKu-W4Avz',
        pdf='https://openreview.net/pdf?id=KNEKu-W4Avz',
        id='F3',
        paper='papers/F3.html',
        proceedings='',
        abstract='MRI is an inherently slow process, which leads to long scan time for high-resolution imaging. The speed of acquisition can be increased by ignoring parts of the data (undersampling). Consequently, this leads to the degradation of image quality. This work proposes a deep learning based MRI reconstruction framework to reconstruct highly undersampled Cartesian or radial MR acquisitions, which includes a modified regularised version of ResNet as the network backbone to remove artefacts from the undersampled image, followed by data consistency steps that fusions the network output with the data already available from undersampled k-space in order to further improve reconstruction quality. The performance of this framework for various undersampling patterns has also been tested, and it has been observed that the framework is robust to deal with various sampling patterns - results in very high quality reconstruction (highest SSIM being 0.990 +/-0.006 for acceleration factor of 3.5), while being compared with the fully sampled reconstruction. It has been shown that the proposed framework can successfully reconstruct even for an acceleration factor of 20 for Cartesian (0.968 +/-0.005) and 17 for radially (0.962 +/-0.012) sampled data. ')
}}
{{ paper('3D Scout Scans Using Projection Domain Denoising',
        'Mikhail Bortnikov, Frank Bergner, Alexey Chernyavskiy, Kevin M. Brown, Noel Black, Michael Grass',
        openreview='https://openreview.net/forum?id=fanGydarIPF',
        pdf='https://openreview.net/pdf?id=fanGydarIPF',
        id='F4',
        paper='papers/F4.html',
        proceedings='',
        abstract='Low dose 2D scouts, also known as topograms, are commonly used for CT scan planning. Although 3D CT volumes can provide more valuable information for the selection of the scan range and parameters, the very low X-ray dose used during scout scan acquisitions results in artefacts requiring effective denoising techniques to make them useful. This has proved challenging for traditional denoising algorithms. We propose a projection domain denoiser based on a convolutional neural network (CNN), which provides improved image quality even at ultra-low dose levels. We compare two CNNs operating on two data representations, a conventional line integral data and raw photon counts, which have different quantitative properties and dynamic ranges. The results show that the two denoising strategies give rise to different properties of reconstructed images and that both projection CNNs are effective for ultra-low dose CT denoising.')
}}
{{ paper('Recurrent Inference Machines as Inverse Problem Solvers for MR Relaxometry',
        'Emanoel Ribeiro Sabidussi, Stefan Klein, Matthan W. A. Caan, Shabab Bazrafkan, Arjan J. den Dekker, Jan Sijbers, Wiro Niessen, Dirk Poot',
        openreview='https://openreview.net/forum?id=h7t0cFuX0m4',
        pdf='https://openreview.net/pdf?id=h7t0cFuX0m4',
        id='F5',
        paper='papers/F5.html',
        proceedings='',
        abstract='In this work, we propose the use of Recurrent Inference Machines (RIMs) to perform T1 mapping. The RIM is a neural network framework that learns an iterative inference process using a model of the signal, similar to conventional statistical methods for quantitative MRI (QMRI), such as the Maximum Likelihood Estimator (MLE). Previously, RIMs were used to solve linear inverse reconstruction problems. Here, we show that they can also be used to optimize non-linear problems. The developed RIM framework is evaluated in terms of accuracy and precision and compared to an MLE method and an implementation of the ResNet. The results show that, compared to the other techniques in Monte Carlo experiments with simulated data, the RIM improves the precision of estimates without compromising in accuracy.')
}}
{{ paper('An artificial intelligence system for predicting the deterioration of COVID-19 patients in the emergency department',
        'Farah Shamout, Yiqiu Shen, Nan Wu, Aakash Kaku, Jungkyu Park, Taro Makino, Stanisław Jastrzębski, Jan Witowski, Duo Wang, Ben Zhang, Siddhant Dogra, Meng Cao, Narges Razavian, David Kudlowitz, Lea Azour, William Moore, Yvonne Lui, Yindalon Aphinyanaphongs, Carlos Fernandez-Granda, Krzysztof J. Geras',
        openreview='https://openreview.net/forum?id=9o6zjvbo7b0',
        pdf='https://openreview.net/pdf?id=9o6zjvbo7b0',
        id='F6',
        paper='papers/F6.html',
        proceedings='',
        abstract='During the COVID-19 pandemic, rapid and accurate triage of patients at the emergency department is critical to inform decision-making. We propose a data-driven approach for prediction of deterioration risk using a deep neural network that learns from chest X-ray images, and a gradient boosting model that learns from routine clinical variables. Our AI prognosis system, trained using data from 3,661 patients, achieves the AUC of 0.786 (95% CI: 0.742-0.827) when predicting deterioration within 96 hours. Our deep neural network indicates informative areas of chest X-ray images to assist clinicians in interpreting the predictions, and performs comparably to two experienced chest radiologists in a reader study. In summary, our findings demonstrate the potential of the proposed system for assisting front-line physicians in the triage of COVID-19 patients.')
}}
{{ paper("ProtoBrainMaps: Prototypical Brain Maps for Alzheimer's Disease Progression Modeling",
        'Ahmad Wisnu Mulyadi, Heung-Il Suk',
        openreview='https://openreview.net/forum?id=O9EWFKXcXTU',
        pdf='https://openreview.net/pdf?id=O9EWFKXcXTU',
        id='F7',
        paper='papers/F7.html',
        proceedings='',
        abstract="Discovering the brain progression over a lifetime is beneficial for identifying the subject affected by neurodegenerative disorders, such as Alzheimer\\'s disease (AD) which require detection at the earliest possible time for the sake of delaying the progression by the virtue of particular treatments. As brain progressions in terms of both normal aging and AD-pathology tend to be entangled to each other, distinguishing the progression pathways of AD over the normal aging brains is quite an intricate task. To this end, we propose Prototypical Brain Maps (ProtoBrainMaps) for modeling the AD progressions through the established prototypes in the latent space via clinically-guided topological maps. Having devised as an interpretable network, it possesses the ability to establish and synthesize a set of well-interpolated prototypical brains, each corresponding to certain health conditions in terms of neurodegenerative diseases. ")
}}
{{ paper('Projection Domain Metal Artifact Reduction in Computed Tomography using Conditional Generative Adversarial Networks',
        'Nele Blum, Thorsten Buzug, Maik Stille',
        openreview='https://openreview.net/forum?id=84NU3uAj1HW',
        pdf='https://openreview.net/pdf?id=84NU3uAj1HW',
        id='F8',
        paper='papers/F8.html',
        proceedings='',
        abstract='High-density objects in the field of view, still remain one of the major challenges in CTimage reconstruction. They cause artifacts in the image, which degrade the quality andthe diagnostic value of the image. Standard approaches for metal artifact reduction areoften unable to correct these artifacts sufficiently or introduce new artifacts. In this work,a new deep learning approach for the reduction of metal artifacts in CT images is proposedusing a Generative Adversarial Network. A generator network is applied directly to theprojection data corrupted by the metal objects to learn the corrected data. In addition, asecond network, the discriminator, is used to evaluate the quality of the learned data. Theresults of the trained generator network show that most of the data could be reasonablyreplaced by the network, reducing the artifacts in the reconstructed image.')
}}
{{ paper('Changing the Contrast of Magnetic Resonance Imaging Signals using Deep Learning',
        'Attila Tibor Simko, Tommy Löfstedt, Anders Garpebring, Mikael Bylund, Tufve Nyholm, Joakim Jonsson',
        openreview='https://openreview.net/forum?id=lWeQH4Kpsys',
        pdf='/proceedings/simko21.pdf',
        id='F9',
        paper='papers/F9.html',
        proceedings='',
        abstract='The contrast settings to select before acquiring magnetic resonance imaging (MRI) signal depend heavily on the subsequent tasks. As each contrast highlights different tissues, automated segmentation tools for example might be optimized for a certain contrast. While for radiotherapy, multiple scans of the same region with different contrasts can achieve a better accuracy for delineating tumours and organs at risk. Unfortunately, the optimal contrast for the subsequent automated methods might not be known during the time of signal acquisition, and performing multiple scans with different contrasts increases the total examination time and registering the sequences introduces extra work and potential errors. Building on the recent achievements of deep learning in medical applications, the presented work describes a novel approach for transferring any contrast to any other.The novel model architecture incorporates the signal equation for spin echo sequences, and hence the model inherently learns the unknown quantitative maps for proton density, T1 and T2 relaxation times (PD, T1 and T2, respectively). This grants the model the ability to retrospectively reconstruct spin echo sequences by changing the contrast settings Echo and Repetition Time (TE and TR, respectively). The model learns to identify the contrast of pelvic MR images, therefore no paired data of the same anatomy from different contrasts is required for training. This means that the experiments are easily reproducible with other contrasts or other patient anatomies.Despite the contrast of the input image, the model achieves accurate results for reconstructing signal with contrasts available for evaluation. For the same anatomy, the quantitative maps are consistent for a range of contrasts of input images. Realized in practice, the proposed method would greatly simplify the modern radiotherapy pipeline. The trained model is made public together with a tool for testing the model on example images.')
}}
[% / %]
<a id="longH"></a><h3>H1-3 (long): Image Acquisition and Reconstruction - 16:00 - 16:30 (UTC+2)</h3>
Chairs: Angelica Aviles-Rivero, Antoine Théberge <br>
[% .papers %]
{{ paper('Hybrid optimization between iterative and network fine-tuning reconstructions for fast quantitative susceptibility mapping',
        'Jinwei Zhang, Hang Zhang, Pascal Spincemaille, Thanh Nguyen, Mert R. Sabuncu, Yi Wang',
        openreview='https://openreview.net/forum?id=LFaxozc7Awm',
        pdf='/proceedings/zhang21d.pdf',
        id='H1',
        paper='papers/H1.html',
        proceedings='',
        abstract='A Hybrid Optimization Between Iterative and network fine-Tuning (HOBIT) reconstruction method is proposed to solve quantitative susceptibility mapping (QSM) inverse problem in MRI. In HOBIT, a convolutional neural network (CNN) is first trained on healthy subjects’ data with gold standard labels. Domain adaptation to patients’ data with hemorrhagic lesions is then deployed by minimizing fidelity loss on the patient training dataset. During test time, a fidelity loss is imposed on each patient test case, where alternating direction method of multiplier (ADMM) is used to split the time consuming fidelity imposed network update into iterative reconstruction and network update subproblems alternatively in ADMM, and only a subnet of the pre-trained CNN is updated during the process. Compared to the method FINE where such fidelity imposing strategy was initially proposed to solve QSM, HOBIT achieved both performance gain of reconstruction accuracy and vast reduction of computational time.')
}}
{{ paper('A Mean-Field Variational Inference Approach to Deep Image Prior for Inverse Problems in Medical Imaging',
        'Malte Tölle, Max-Heinrich Laves, Alexander Schlaefer',
        openreview='https://openreview.net/forum?id=DvV_blKLiB4',
        pdf='/proceedings/toelle21.pdf',
        id='H2',
        paper='papers/H2.html',
        proceedings='',
        abstract='Exploiting the deep image prior property of convolutional auto-encoder networks is especially interesting for medical image processing as it avoids hallucinations by omitting supervised learning. Its spectral bias towards lower frequencies makes it suitable for inverse image problems such as denoising and super-resolution, but manual early stopping has to be applied to act as a low-pass filter. In this paper, we present a novel Bayesian approach to deep image prior using mean-field variational inference. This allows for uncertainty quantification on a per-pixel level and, given the right prior distribution on the network weights, omits the need for early stopping. We optimize the parameters of the weight prior towards reconstruction accuracy using Bayesian optimization with Gaussian Process regression. We evaluate our approach on different inverse tasks on a variety of modalities and demonstrate that an optimized weight prior outperforms former state-of-the-art Bayesian deep image prior approaches. We show that a badly selected prior leads to worse accuracy and calibration and that it is sufficient to optimize the weight prior parameter per task domain.')
}}
{{ paper('Residual learning for 3D motion corrected quantitative MRI: Robust clinical T1, T2 and proton density mapping',
        'Carolin Pirkl, Matteo Cencini, Jan W. Kurzawski, Diana Waldmannstetter, Hongwei Li, Anjany Sekuboyina, Sebastian Endt, Luca Peretti, Graziella Donatelli, Rosa Pasquariello, Michela Tosetti, Mauro Costagli, Guido Buonincontri, Marion Menzel, bjoern menze',
        openreview='https://openreview.net/forum?id=hxgQM71AuRA',
        pdf='/proceedings/pirkl21.pdf',
        id='H3',
        paper='papers/H3.html',
        proceedings='',
        abstract='Subject motion is one of the major challenges in clinical routine MR imaging. Despite ongoing research, motion correction has remained a complex problem without a universal solution. In advanced quantitative MR techniques, such as MR Fingerprinting, motion does not only affect a single image, like in single-contrast MRI, but disrupts the entire temporal evolution of the magnetization and causes parameter quantification errors due to a mismatch between the acquired and simulated signals. In this work, we present a deep learning-empowered retrospective motion correction for rapid 3D whole-brain multiparametric MRI based on Quantitative Transient-state Imaging (QTI). We propose a patch-based 3D multiscale convolutional neural network (CNN) that learns the residual error, i.e. after initial navigator-based correction, between motion-affected quantitative T1, T2 and proton density maps and their motion-free counterparts. For efficient model training despite limited data availability, we propose a physics-informed simulation to apply continuous motion-patterns to motion-free data. We evaluate the performance of the residual CNN on 1.5T and 3T MRI data of ten healthy volunteers. We analyze the generalizability of the model when applied to real clinical cases, including pediatric and adult patients with large brain lesions. Our study demonstrates that image quality can be significantly improved after correcting for subject motion. This has important implications in clinical setups where large amounts of motion affected data must be discarded.')
}}
[% / %]
<a id="shortG"></a><h3>G1-9 (short): Interpretability and Explainable AI - 16:45 - 17:30 (UTC+2)</h3>
Chairs: Monika Grewal, Christian Ledig <br>
[% .papers %]
{{ paper('Me-NDT: Neural-backed Decision Tree for Visual Explainability of Deep Medical Models',
        'Guanghui FU, Ruiqian Wang, Jianqiang Li, Maria Vakalopoulou, Vicky Kalogeiton',
        openreview='https://openreview.net/forum?id=pL_aFZKNO5N',
        pdf='https://openreview.net/pdf?id=pL_aFZKNO5N',
        id='G1',
        paper='papers/G1.html',
        proceedings='',
        abstract='Despite the progress of deep learning on medical imaging, there is still not a true understanding of what networks learn and of how decisions are reached. Here, we address this by proposing a Visualized Neural-backed Decision Tree for Medical image analysis, Me-NDT. It is a CNN with a tree-based structure template that allows for both classification and visualization of firing neurons, thus offering interpretability. We also introduce node and path losses that allow Me-NDT to consider the entire path instead of isolated nodes. Our experiments on brain CT and chest radiographs outperform all baselines. Overall, Me-NDT is a lighter, comprehensively explanatory model, of great value for clinical practice. ')
}}
{{ paper('ICAM-reg: Interpretable Classification and Regression with Feature Attribution for Mapping Neurological Phenotypes in Individual Scans',
        'Cher Bass, Mariana da Silva, Carole H. Sudre, Logan Zane John Williams, Petru-Daniel Tudosiu, Fidel Alfaro-Almagro, Sean P. Fitzgibbon, Matthew Glasser, Stephen M. Smith, Emma Claire Robinson',
        openreview='https://openreview.net/forum?id=164F3ixC9Jc',
        pdf='https://openreview.net/pdf?id=164F3ixC9Jc',
        id='G2',
        paper='papers/G2.html',
        proceedings='',
        abstract='Feature attribution (FA), or the assignment of class-relevance to different locations in an image, is important for many classification and regression problems but is particularly crucial within the neuroscience domain, where accurate mechanistic models of behaviours, or disease, require knowledge of all features discriminative of a trait. At the same time, predicting class relevance from brain images is challenging as phenotypes are typically heterogeneous, and changes occur against a background of significant natural variation.  Here, we present an extension of the ICAM framework for creating prediction specific FA maps through image-to-image translation.')
}}
{{ paper('Radiographic Assessment of CVC Malpositioning: How can AI best support clinicians?',
        'Lasse Hansen, Malte Sieren, Malte Hobe, Axel Saalbach, Heinrich Schulz, Jörg Barkhausen, Mattias P Heinrich',
        openreview='https://openreview.net/forum?id=ImcP8kkqtfZ',
        pdf='https://openreview.net/pdf?id=ImcP8kkqtfZ',
        id='G3',
        paper='papers/G3.html',
        proceedings='',
        abstract='The malpositioning of central venous catheters (CVCs) is a common technical complication that is usually diagnosed on post-procedure chest X-rays (CXRs). If the misplaced CVC remains undetected, it can lead to serious health consequences for the patient. Interpreting CXRs at a large scale in everyday clinical practice is time consuming and can create delays in the repositioning of the CVC. A computer-assisted assessment of post-procedure CXRs can help to prioritise cases and reduce human errors in stressful situations by objectifying decisions. However, final assessments must always be made by the clinicians, which is why the algorithmic support needs to be comprehensible.Since AI models are not yet able to detect catheter maplpositons with highest accuracy, the focus must be on efficient support in everyday clinical practice. In this work, we evaluate three different AI models, particularly with regard to the relationship between classification accuracy and the degree of explainability. Our results show how helpful it is to incorporate explicit clinical knowledge into deep learning-based models and give us promising research directions for a planned large scale patient study.')
}}
{{ paper('Test-Time Mixup Augmentation for Uncertainty Estimation in Skin Lesion Diagnosis',
        'Hansang Lee, Haeil Lee, Helen Hong, Junmo Kim',
        openreview='https://openreview.net/forum?id=aGfL5C9wRx_',
        pdf='https://openreview.net/pdf?id=aGfL5C9wRx_',
        id='G4',
        paper='papers/G4.html',
        proceedings='',
        abstract='Uncertainty is considered to be an important measure that provides valuable information on the learning behavior of deep neural networks. In this paper, we propose an uncertainty estimation method using test-time mixup augmentation (TTMA). The TTMA uncertainty is obtained by replacing affine augmentation with the mixup in the existing test-time augmentation (TTA) method. In addition to the data uncertainty, we propose TTMA-based class-specific uncertainty, which can provide information on between-class confusion. In experiments on the skin lesion diagnosis dataset, we confirmed that the proposed TTMA not only provides better epistemic uncertainty than TTA but also provides information on between-class confusion through class-specific uncertainty.')
}}
{{ paper('Interpretable Medical Image Classification with Self-Supervised Anatomical Embedding and Prior Knowledge',
        'Ke Yan, Youbao Tang, Adam P Harrison, Jinzheng Cai, Le Lu, Jingjing Lu',
        openreview='https://openreview.net/forum?id=0wblcjbC2sN',
        pdf='https://openreview.net/pdf?id=0wblcjbC2sN',
        id='G5',
        paper='papers/G5.html',
        proceedings='',
        abstract='In medical image analysis tasks, it is important to make machine learning models focus on correct anatomical locations, so as to improve interpretability and robustness of the model. We adopt a latest algorithm called self-supervised anatomical embedding (SAM) to locate point of interest (POI) on computed tomography (CT) scans. SAM can detect arbitrary POI with only one labeled sample needed. Then, we can extract targeted features from the POIs to train a simple prediction model guided by clinical prior knowledge. This approach mimics the practice of human radiologists, thus is interpretable, controllable, and robust. We illustrate our approach on the application of CT contrast phase classification and it outperforms an existing deep learning based method trained on the whole image.')
}}
{{ paper('50 shades of overfitting:  towards MRI-based neurologicalmodels interpretation',
        'Polina Druzhinina, Ekaterina Kondrateva, Evgeny Burnaev',
        openreview='https://openreview.net/forum?id=fnb58KJtYv',
        pdf='https://openreview.net/pdf?id=fnb58KJtYv',
        id='G6',
        paper='papers/G6.html',
        proceedings='',
        abstract="MRI-based prediction models are one of the most exploited AI solutions in neurology. Numerous computer-vision models showed their predictive ability for diverse psychoneurological conditions. Although most of these models are based on weak or no annotation, only a few reported studies interpret the predictions and perform the model saliency regions\\' analysis.We utilize 3DCNN interpretation with GradCAM to explore learned patterns for basic demographic characteristics prediction on the healthy cohort. We compare the saliency maps of the gender prediction models with the different types of MRI data preprocessing and augmentation. We assess the quality of learned patterns and examine the ways of models overfitting. We propose a data augmentation strategy based on optimal transport to avoid model overfitting on the brain volumes.")
}}
{{ paper('Weakly-supervised High-resolution Segmentation of Mammography Images for Breast Cancer Diagnosis',
        'Kangning Liu, Yiqiu Shen, Nan Wu, Jakub Piotr Chłędowski, Carlos Fernandez-Granda, Krzysztof J. Geras',
        openreview='https://openreview.net/forum?id=nBT8eNF7aXr',
        pdf='/proceedings/liu21b.pdf',
        id='G7',
        paper='papers/G7.html',
        proceedings='',
        abstract='In the last few years, deep learning classifiers have shown promising results in image-based medical diagnosis. However, interpreting the outputs of these models remains a challenge. In cancer diagnosis, interpretability can be achieved by localizing the region of the input image responsible for the output, i.e. the location of a lesion. Alternatively, segmentation or detection models can be trained with pixel-wise annotations indicating the locations of malignant lesions. Unfortunately, acquiring such labels is labor-intensive and requires medical expertise. To overcome this difficulty, weakly-supervised localization can be utilized. These methods allow neural network classifiers to output saliency maps highlighting the regions of the input most relevant to the classification task (e.g. malignant lesions in mammograms) using only image-level labels (e.g. whether the patient has cancer or not) during training. When applied to high-resolution images, existing methods produce low-resolution saliency maps. This is problematic in applications in which suspicious lesions are small in relation to the image size. In this work, we introduce a novel neural network architecture to perform weakly-supervised segmentation of high-resolution images. The proposed model selects regions of interest via coarse-level localization, and then performs fine-grained segmentation of those regions.We apply this model to breast cancer diagnosis with screening mammography, and validate it on a large clinically-realistic dataset. Measured by Dice similarity score, our approach outperforms existing methods by a large margin in terms of localization performance of benign and malignant lesions, relatively improving the performance by 39.6% and 20.0%, respectively. Code and the weights of some of the models are available at https://github.com/nyukat/GLAM')
}}
{{ paper('The OOD Blind Spot of Unsupervised Anomaly Detection',
        'Matthäus Heer, Janis Postels, Xiaoran Chen, Ender Konukoglu, Shadi Albarqouni',
        openreview='https://openreview.net/forum?id=ZDD2TbZn7X1',
        pdf='/proceedings/heer21.pdf',
        id='G8',
        paper='papers/G8.html',
        proceedings='',
        abstract='Deep unsupervised generative models are regarded as a promising alternative to supervised counterparts in the field of MRI-based lesion detection. They denote a principled approach for detecting unseen types of anomalies without relying on large amounts of expensive ground truth annotations. To this end, deep generative models are trained exclusively on data from healthy patients and detect lesions as  Out-of-Distribution (OOD) data at test time (i.e. low likelihood). While this is a promising way of bypassing the need for costly annotations, this work demonstrates that it also renders this widely used unsupervised anomaly detection approach particularly vulnerable to non-lesion-based OOD data (e.g. data from different sensors). Since models are likely to be exposed to such OOD data in production, it is crucial to employ safety mechanisms to filter for such samples and run inference only on input for which the model is able to provide reliable results. We first show extensively that conventional, unsupervised anomaly detection mechanisms fail when being presented with true OOD data. Secondly, we apply prior knowledge to disentangle lesion-based OOD from their non-lesion-based counterparts.')
}}
{{ paper('A regularization term for slide correlation reduction in whole slide image analysis with deep learning',
        'Hongrun Zhang, Yanda Meng, Xuesheng Qian, Xiaoyun Yang, Sarah E Coupland, Yalin Zheng',
        openreview='https://openreview.net/forum?id=2vCFIoWDS6E',
        pdf='/proceedings/zhang21a.pdf',
        id='G9',
        paper='papers/G9.html',
        proceedings='',
        abstract='To develop deep learning-based models for automatic analysis of histopathology whole slide images (WSIs), the atomic entities to be directly processed are often the smaller patches cropped from WSIs as it is not always possible to feed a whole WSI to a model given its enormous size. However, a trained model tends to relate the slide-specific characteristics to diagnosis results because a large number of patches cropped from the same WSI will  share common slide features and thus have strong correlations between them, resulting in deteriorated generalization capability of the trained model. Current approaches to alleviate this issue include data pre-processing (stain normalization or color augmentation) and adversarial learning, both of which introduce extra complications in computations. Alternatively, we propose to reduce the impact of this issue by introducing a new regularization term to the standard loss function to reduce the correlation of the patches from the same WSI. It is intuitive and easy-to-implement and introduces comparably smaller  computation overhead compared to existing approaches. Experimental results prove that the proposed regularization term is able to enhance the generalization capability of learning models and consequently to achieve better performance. The code is available in:  \\url{https://github.com/hrzhang1123/SlideCorrelationReduction}.')
}}
[% / %]
<a id="shortH"></a><h3>H4-12 (short): Application: Radiology - 16:45 - 17:30 (UTC+2)</h3>
Chairs: Raghav Mehta, Clarisa Sanchez <br>
[% .papers %]
{{ paper('Optimizing Operating Points for High Performance Lesion Detection and Segmentation Using Lesion Size Reweighting',
        'Brennan Nichyporuk, Justin Szeto, Douglas Arnold, Tal Arbel',
        openreview='https://openreview.net/forum?id=yVYVzsNWvN',
        pdf='https://openreview.net/pdf?id=yVYVzsNWvN',
        id='H4',
        paper='papers/H4.html',
        proceedings='',
        abstract='There are many clinical contexts which require accurate detection and segmentation of all focal pathologies (e.g. lesions, tumours) in patient images. In cases where there are a mix of small and large lesions, standard binary cross entropy loss will result in better segmentation of large lesions at the expense of missing small ones. Adjusting the operating point to accurately detect all lesions generally leads to oversegmentation of large lesions. In this work, we propose a novel reweighing strategy to eliminate this performance gap, increasing small pathology detection performance while maintaining segmentation accuracy. We show that our reweighing strategy vastly outperforms competing strategies based on experiments on a large scale, multi-scanner, multi-center dataset of Multiple Sclerosis patient images.')
}}
{{ paper('Creating Anthropomorphic Phantoms via Unsupervised Convolutional Neural Networks',
        'Junyu Chen, Ye Li, Yong Du, Eric Frey',
        openreview='https://openreview.net/forum?id=xqZTapYnEcG',
        pdf='https://openreview.net/pdf?id=xqZTapYnEcG',
        id='H5',
        paper='papers/H5.html',
        proceedings='',
        abstract='Computerized phantoms play an important role in medical imaging research. They can serve as a gold standard for evaluating and optimizing medical imaging analysis, processing, and reconstruction methods. Existing computerized phantoms model anatomical variations through organ and phantom scaling, which does not fully capture the range of anatomical variations seen in humans. Here, we present a registration-based method for creating highly realistic and detailed anthropomorphic phantoms. The proposed registration method is built on the use of an unsupervised convolutional neural network (ConvNet) that warps the four-dimensional Xtended Cardiac-Torso (XCAT) phantom to a patient CT scan. The registration ConvNet iteratively optimizes an SSIM-based loss function for a given image pair without prior training. We experimentally show substantially improved image similarity of the generated phantom using the proposed method to a patient image.')
}}
{{ paper('Transformers for Ischemic Stroke Infarct Core Segmentation from Spatio-temporal CT Perfusion Scans',
        'Lucas de Vries, Bart Emmer, Charles Majoie, Henk Marquering, Efstratios Gavves',
        openreview='https://openreview.net/forum?id=CSNQMsxteqm',
        pdf='https://openreview.net/pdf?id=CSNQMsxteqm',
        id='H6',
        paper='papers/H6.html',
        proceedings='',
        abstract='The infarct core size is a crucial biomarker for treatment selection for ischemic stroke patients. For this purpose, we present a novel approach to perform infarct core segmentation using CT perfusion (CTP) source data, without ordinary deconvolution analysis. We propose the use of transformers to encode sequential CTP scans in spatial attention maps, which we subsequently use for infarct core segmentation. We report new top results on the ISLES 2018 challenge test data set for infarct core segmentation. This work presents a primary benchmark for infarct core segmentation from CTP source data using transformers.')
}}
{{ paper('Multichannel input pixelwise regression 3D U-Nets for medical image estimation with 3 applications in brain MRI',
        'Jueqi Wang, Derek Berger, David Mattie, Jacob Levman',
        openreview='https://openreview.net/forum?id=JG895xlWsfA',
        pdf='https://openreview.net/pdf?id=JG895xlWsfA',
        id='H7',
        paper='papers/H7.html',
        proceedings='',
        abstract="The U-Net is a robust general-purpose deep learning architecture designed for semantic segmentation of medical images, and has been extended to 3D for volumetric applications such as magnetic resonance imaging (MRI) of the human brain. An adaptation of the U-Net to output pixelwise regression values, instead of class labels, based on multichannel input data, has been developed in the remote sensing satellite imaging research domain. The pixelwise regression U-Net has only received limited consideration as a deep learning architecture in medical imaging for the image estimation/synthesis problem, and the limited work so far did not consider the application of 3D multichannel inputs. In this paper, we propose the use of the multichannel input pixelwise regression 3D U-Net (rUNet) for estimation of medical images. Our findings demonstrate that this approach is robust and versatile and can be applied to predicting a pending MRI examination of patients with Alzheimer\\'s disease based on previous rounds of imaging, can perform medical image reconstruction (parametric mapping) in diffusion MRI, and can be applied to the estimation of one type of MRI examination from a collection of other types. Results demonstrate that the rUNet represents a single deep learning architecture capable of solving a variety of image estimation problems. Public domain code is provided.")
}}
{{ paper('Morphology-based losses for weakly supervised segmentation of mammograms',
        'Mickael Tardy, Diana Mateus',
        openreview='https://openreview.net/forum?id=eehADvdlUa3',
        pdf='https://openreview.net/pdf?id=eehADvdlUa3',
        id='H8',
        paper='papers/H8.html',
        proceedings='',
        abstract='Segmentation is one of the most common tasks in medical imaging, but it often requires expensive ground truth for training. Weakly supervised methods cope with the lack of annotations, however, they often fall short compared to fully supervised ones. In this work, we propose to constrain the segmentation output with morphological operations, leading to an increase in the overall performance. In particular, we use top-hat and closing operations. We evaluate the method on high-resolution images from INBreast dataset and achieve an increase in F1 of approx. 0.14 and in recall of approx. 0.22 compared to the training without morphology loss.')
}}
{{ paper('Partial Convolution Network for Metal Artifact Reduction in CT Preprocessing: Preliminary Results',
        'Laura Hellwege, Nele Blum, Thorsten Buzug, Maik Stille',
        openreview='https://openreview.net/forum?id=XCRthDLsCXn',
        pdf='https://openreview.net/pdf?id=XCRthDLsCXn',
        id='H9',
        paper='papers/H9.html',
        proceedings='',
        abstract='Metal artifacts impair the diagnostic value of medical CT images. These artifacts occur from the projection values associated with the metal objects inside the scanned anatomy. In this work, we replace the corrupted projection values by using a deep convolutional neural network consisting of so-called partial convolution layers. We show that the network trained on simulated data enhances newly presented projection data and therefore the corresponding reconstructed image. ')
}}
{{ paper('A Surprisingly Effective Perimeter-based Loss for Medical Image Segmentation',
        'Rosana EL Jurdi, Caroline Petitjean, Paul Honeine, Veronika Cheplygina, Fahed Abdallah',
        openreview='https://openreview.net/forum?id=NDEmtyb4cXu',
        pdf='/proceedings/eljurdi21.pdf',
        id='H10',
        paper='papers/H10.html',
        proceedings='',
        abstract='Deep convolutional networks recently made many breakthroughs in medical image segmentation. Still, some anatomical artefacts may be observed in the segmentation results, with holes or inaccuracies near the object boundaries. To address these issues, loss functions that incorporate constraints, such as spatial information or prior knowledge, have been introduced. An example of such prior losses are the contour-based losses, which exploit distance maps to conduct point-by-point optimization between ground-truth and predicted contours. However, such losses may be computationally expensive or susceptible to trivial local solutions and vanishing gradient problems. Moreover, they depend on distance maps which tend to underestimate the contour-to-contour distances. We propose a novel loss constraint that optimizes the perimeter length of the segmented object relative to the ground-truth segmentation. The novelty lies in computing the perimeter with a soft approximation of the contour of the probability map via specialized non-trainable layers in the network. Moreover, we optimize the mean squared error between the predicted perimeter length and ground-truth perimeter length. This soft optimization of contour boundaries allows the network to take into consideration border irregularities within organs while still being efficient. Our experiments on three public datasets (spleen, hippocampus and cardiac structures) show that the proposed method outperforms state-of-the-art boundary losses for both single and multi-organ segmentation.')
}}

{{ paper('Unseen Disease Detection for Deep Learning Interpretation of Chest X-rays',
        'Siyu Shi, Ishaan Malhi, Kevin Tran, Andrew Y. Ng, Pranav Rajpurkar',
        openreview='https://openreview.net/forum?id=i-zxSlqneRu',
        pdf='/proceedings/shi21.pdf',
        id='H12',
        paper='papers/H12.html',
        proceedings='',
        abstract="We systematically evaluate the performance of deep learning models in the presence of diseases not labeled for or present during training. First, we evaluate whether deep learning models trained on a subset of diseases (seen diseases) can detect the presence of any one of a larger set of diseases. We find that models tend to falsely classify diseases outside of the subset (unseen diseases) as no disease\\'\\'. Second, we evaluate whether models trained on seen diseases can detect seen diseases when co-occurring with diseases outside the subset (unseen diseases). We find that models are still able to detect seen diseases even when co-occurring with unseen diseases. Third, we evaluate whether feature representations learned by models may be used to detect the presence of unseen diseases given a small labeled set of unseen diseases. We find that the penultimate layer provides useful features for unseen disease detection. Our results can inform the safe clinical deployment of deep learning models trained on a non-exhaustive set of disease classes.")
}}
[% / %]

<hr>

<h2> Friday 9th July</h2>
<a id="longI"></a><h3>I1-3 (long): Interpretability and Explainable AI - 13:00 - 13:30 (UTC+2)</h3>
Chairs: Ismail Ben Ayed, Arrate Muñoz-Barrutia <br>
[% .papers %]
{{ paper('Explainable Image Quality Analysis of Chest X-Rays',
        'Caner Ozer, Ilkay Oksuz',
        openreview='https://openreview.net/forum?id=ln797A8lAb0',
        pdf='/proceedings/ozer21.pdf',
        id='I1',
        paper='papers/I1.html',
        proceedings='',
        abstract='Medical image quality assessment is an important aspect of image acquisition where poor-quality images may lead to misdiagnosis. In addition, manual labelling of image quality after the acquisition is often tedious and can lead to some misleading results. Despite much research on the automated analysis of image quality for tackling this problem, relatively little work has been done for the explanation of the methodologies. In this work, we propose an explainable image quality assessment system and validate our idea on foreign objects in a Chest X-Ray (Object-CXR) dataset. Our explainable pipeline relies on NormGrad, an algorithm, which can efficiently localize the image quality issues with saliency maps of the classifier. We compare our method with a range of saliency detection methods and illustrate the superior performance of NormGrad by obtaining a Pointing Game accuracy of 0.862 on the test dataset of the Object-CXR dataset. We also verify our findings through a qualitative analysis by visualizing attention maps for foreign objects on X-Ray images.')
}}
{{ paper('Gifsplanation via Latent Shift: A Simple Autoencoder Approach to Counterfactual Generation for Chest X-rays',
        'Joseph Paul Cohen, Rupert Brooks, Sovann En, Evan Zucker, Anuj Pareek, Matthew P. Lungren, Akshay Chaudhari',
        openreview='https://openreview.net/forum?id=rnunjvgxAMt',
        pdf='/proceedings/cohen21.pdf',
        id='I2',
        paper='papers/I2.html',
        proceedings='',
        abstract='Motivation: Traditional image attribution methods struggle to satisfactorily explain predictions of neural networks. Prediction explanation is important, especially in medical imaging, for avoiding the unintended consequences of deploying AI systems when false positive predictions can impact patient care. Thus, there is a pressing need to develop improved models for model explainability and introspection. Specific problem: A new approach is to transform input images to increase or decrease features which cause the prediction. However, current approaches are difficult to implement as they are monolithic or rely on GANs. These hurdles prevent wide adoption.Our approach: Given an arbitrary classifier, we propose a simple autoencoder and gradient update (Latent Shift) that can transform the latent representation of a specific input image to exaggerate or curtail the features used for prediction. We use this method to study chest X-ray classifiers and evaluate their performance. We conduct a reader study with two radiologists assessing 240 chest X-ray predictions to identify which ones are false positives (half are) using traditional attribution maps or our proposed method.Results: We found low overlap with ground truth pathology masks for models with reasonably high accuracy. However, the results from our reader study indicate that these models are generally looking at the correct features.We also found that the Latent Shift explanation allows a user to have more confidence in true positive predictions compared to traditional approaches (0.15±0.95 in a 5 point scale with p=0.01) with only a small increase in false positive predictions (0.04±1.06 with p=0.57).Accompanying webpage: https://mlmed.org/gifsplanation/Source code: https://github.com/mlmed/gifsplanation')
}}
{{ paper('Understanding and Visualizing Generalization UNets',
        'Abhejit Rajagopal, Vamshi Chowdary Madala, Thomas A Hope, Peder Larson',
        openreview='https://openreview.net/forum?id=V-a5DJCh4Hk',
        pdf='/proceedings/rajagopal21.pdf',
        id='I3',
        paper='papers/I3.html',
        proceedings='',
        abstract="Fully-convolutional neural networks, such as the 2D or 3D UNet, are now pervasive in medical imaging for semantic segmentation, classification, image denoising, domain translation, and reconstruction. However, evaluation of UNet performance, as with most CNNs, has mostly been relegated to evaluation of a few performance metrics (e.g. accuracy, IoU, SSIM, etc.) using the network\\'s final predictions, which provides little insight into important issues such as dataset shift that occur in clinical application. In this paper, we propose techniques for understanding and visualizing the generalization performance of UNets in image classification and regression tasks, giving rise to metrics that are indicative of performance on a withheld test-set without the need for groundtruth annotations.")
}}
[% / %]
<a id="shortI"></a><h3>I4-12 (short): Transfer Learning and Domain Adaptation - 13:45 - 14:30 (UTC+2)</h3>
Chairs: Katharina Breininger, Maria Vakalopoulou <br>
[% .papers %]
{{ paper('Scopeformer: n-CNN-ViT hybrid model for Intracranial hemorrhage subtypes classification',
        'Yassine Barhoumi, Ghulam Rasool',
        openreview='https://openreview.net/forum?id=M1VznPOV5jV',
        pdf='https://openreview.net/pdf?id=M1VznPOV5jV',
        id='I4',
        paper='papers/I4.html',
        proceedings='',
        abstract='We propose a feature generator backbone composed of an ensemble of convolutional neural networks (CNNs) to improve the recently emerging Vision Transformer (ViT) models. We tackled the RSNA intracranial hemorrhage classification problem, i.e., identifying various hemorrhage  types  from  computed  tomography  (CT)  slices.   We  show  that  by gradually stacking  several  feature  maps  extracted  using  multiple  Xception  CNNs,  we  can develop a  feature-rich  input  for  the  ViT  model.   Our  approach  allowed  the  ViT  model  to  pay attention to relevant features at multiple levels.  Moreover, pretraining the ”n” CNNs using various paradigms leads to a diverse feature set and further improves the performance of the proposed n-CNN-ViT. We achieved a test accuracy of 98.04% with a weighted logarithmic loss value of 0.0708.  The proposed architecture is modular and scalable in both the number of CNNs used for feature extraction and the size of the ViT.')
}}
{{ paper('Robust medical image segmentation by adapting neural networks for each test image',
        'Neerav Karani, Ertunc Erdil, Krishna Chaitanya, Ender Konukoglu',
        openreview='https://openreview.net/forum?id=tv_pkmFzdC',
        pdf='https://openreview.net/pdf?id=tv_pkmFzdC',
        id='I5',
        paper='papers/I5.html',
        proceedings='',
        abstract='Performance of convolutional neural networks (CNNs) used for medical image analyses degrades markedly when training and test images differ in terms of their acquisition details, such as the scanner model or the protocol. We tackle this issue for the task of image segmentation by adapting a CNN (C) for each test image. Specifically, we design C as a concatenation of a shallow normalization CNN (N), followed by a deep CNN (S) that segments the normalized image. At test time, we adapt N for each test image, guided by an implicit prior on the predicted labels, which is modelled using an independently trained denoising autoencoder (D). The method is validated on multi-center MRI datasets of 3 anatomies. This article is a short version of the journal paper~\\cite{karani2021test}.')
}}
{{ paper('Quantifying the Scanner-Induced Domain Gap in Mitosis Detection',
        'Marc Aubreville',
        openreview='https://openreview.net/forum?id=OcATYbGIxv4',
        pdf='https://openreview.net/pdf?id=OcATYbGIxv4',
        id='I6',
        paper='papers/I6.html',
        proceedings='',
        abstract='Automated detection of mitotic figures in histopathology images has seen vast improvements, thanks to modern deep learning-based pipelines. Application of these methods, however, is in practice limited by strong variability of images between labs. This results in a domain shift of the images, which causes a performance drop of the models. Hypothesizing that the scanner device plays a decisive role in this effect, we evaluated the susceptibility of a standard mitosis detection approach to the domain shift introduced by using a different whole slide scanner. Our work is based on the MICCAI-MIDOG challenge 2021 data set, which includes 200 tumor cases of human breast cancer and four scanners.  Our work indicates that the domain shift induced not by biochemical variability but purely by the choice of acquisition device is underestimated so far. Models trained on images of the same scanner yielded an average F1 score of 0.683, while models trained on a single other scanner only yielded an average F1 score of 0.325. Training on another multi-domain mitosis dataset led to mean F1 scores of 0.52. We found this not to be reflected by domain-shifts measured as proxy A distance-derived metric.')
}}
{{ paper('Echocardiographic Phase Detection Using Neural Networks',
        'Elisabeth Sarah Lane, Neda Azarmehr, Jevgeni Jevsikov, James P Howard, Matthew Shun-shin, Darrel P Francis, Massoud Zolgharni',
        openreview='https://openreview.net/forum?id=uEuoKy2hUkm',
        pdf='https://openreview.net/pdf?id=uEuoKy2hUkm',
        id='I7',
        paper='papers/I7.html',
        proceedings='',
        abstract='Accurate identification of end-diastolic and end-systolic frames in echocardiographic cine loops is essential when measuring cardiac function. Manual selection by human experts is challenging and error prone. This paper presents a deep neural network trained and tested on multi-centre patient data for accurate phase detection in apical four-chamber videos of arbitrary length, spanning several heartbeats, with performance indistinguishable from that of human experts.')
}}
{{ paper('HAD-Net: A Hierarchical Adversarial Knowledge Distillation Network for Improved Enhanced Tumour Segmentation Without Post-Contrast Images',
        'Saverio Vadacchino, Raghav Mehta, Nazanin Mohammadi Sepahvand, Brennan Nichyporuk, James J. Clark, Tal Arbel',
        openreview='https://openreview.net/forum?id=48UgSFrNR2',
        pdf='/proceedings/vadacchino21.pdf',
        id='I8',
        paper='papers/I8.html',
        proceedings='',
        abstract='Segmentation of enhancing tumours or lesions from MRI is important for detecting new disease activity in many clinical contexts. However, accurate segmentation requires the inclusion of medical images (e.g., T1 post-contrast MRI) acquired after injecting patients with a contrast agent (e.g., Gadolinium), a process no longer thought to be safe. Although a number of modality-agnostic segmentation networks have been developed over the past few years, they have been met with limited success in the context of enhancing pathology segmentation. In this work, we present HAD-Net, a novel offline adversarial knowledge distillation (KD) technique, whereby a pre-trained teacher segmentation network, with access to all MRI sequences, teaches a student network, via hierarchical adversarial training, to better overcome the large domain shift presented when crucial images are absent during inference. In particular, we apply HAD-Net to the challenging task of enhancing tumour segmentation when access to post-contrast imaging is not available. The proposed network is trained and tested on the BraTS 2019 brain tumour segmentation challenge dataset, where it achieves performance improvements in the ranges of 16% - 26% over (a) recent modality-agnostic segmentation methods (U-HeMIS, U-HVED), (b) KD-Net adapted to this problem, (c) the pre-trained student network and (d) a non-hierarchical version of the network (AD-Net), in terms of Dice scores for enhancing tumour (ET). The network also shows improvements in tumour core (TC) Dice scores. Finally, the network outperforms both the baseline student network and AD-Net in terms of uncertainty quantification for enhancing tumour segmentation based on the BraTS 2019 uncertainty challenge metrics. Our code is publicly available at: https://github.com/SaverioVad/HAD_Net')
}}
{{ paper('An MRF-UNet Product of Experts for Image Segmentation',
        'Mikael Brudfors, Yaël Balbastre, John Ashburner, Geraint Rees, Parashkev Nachev, Sebastien Ourselin, M. Jorge Cardoso',
        openreview='https://openreview.net/forum?id=PoIV8EXQDjn',
        pdf='/proceedings/brudfors21.pdf',
        id='I9',
        paper='papers/I9.html',
        proceedings='',
        abstract='While convolutional neural networks (CNNs) trained by back-propagation have seen unprecedented success at semantic  segmentation tasks, they are known to struggle on out-of-distribution data. Markov random fields (MRFs) on the other hand, encode simpler distributions over labels that, although less flexible than UNets, are less prone to over-fitting. In this paper, we propose to fuse both strategies by computing the product of distributions of a UNet and an MRF. As this product is intractable, we solve for an approximate distribution using an iterative mean-field approach. The resulting MRF-UNet is trained jointly by back-propagation. Compared to other works using conditional random fields (CRFs), the MRF has no dependency on the imaging data, which should allow for less over-fitting. We show on 3D neuroimaging data that this novel network improves generalisation to out-of-distribution samples. Furthermore, it allows the overall number of parameters to be reduced while preserving high accuracy. These results suggest that a classic MRF smoothness prior can allow for less over-fitting when principally integrated into a CNN model. Our implementation is available at https://github.com/balbasty/nitorch.')
}}
{{ paper('Partial transfusion: on the expressive influence of trainable batch norm parameters for transfer learning',
        'Fahdi Kanavati, Masayuki Tsuneki',
        openreview='https://openreview.net/forum?id=TjwDWRdfZpg',
        pdf='/proceedings/kanavati21.pdf',
        id='I10',
        paper='papers/I10.html',
        proceedings='',
        abstract='Transfer learning from ImageNet is the go-to approach when applying deep learning to medical images. The approach is either to fine-tune a pre-trained model or use it as a feature extractor.Most modern architecture contain batch normalisation layers, and fine-tuning a model with such layers requires taking a few precautions as they consist of trainable and non-trainable weights and have two operating modes: training and inference. Attention is primarily given to the non-trainable weights used during inference, as they are the primary source of unexpected behaviour or degradation in performance during transfer learning. It is typically recommended to fine-tune the model with the batch normalisation layers kept in inference mode during both training and inference. In this paper, we pay closer attention instead to the trainable weights of the batch normalisation layers, and we explore their expressive influence in the context of transfer learning.We find that only fine-tuning the trainable weights (scale and centre) of the batch normalisation layers leads to similar performance as to fine-tuning all of the weights, with the added benefit of faster convergence. We demonstrate this on a variety of seven publicly available medical imaging datasets, using four different model architectures. ')
}}
{{ paper('CNN and Deep Sets for End-to-End Whole Slide Image Representation Learning',
        'Sobhan Hemati, Shivam Kalra, Cameron Meaney, Morteza Babaie, Ali Ghodsi, Hamid Tizhoosh',
        openreview='https://openreview.net/forum?id=BX0kKB1zB1Q',
        pdf='/proceedings/hemati21.pdf',
        id='I11',
        paper='papers/I11.html',
        proceedings='',
        abstract='Digital pathology has enabled us to capture, store and analyze scanned biopsy samples as digital images. Recent advances in deep learning are contributing to computational pathology to improve diagnosis and treatment. However, considering challenges inherent to whole slide images (WSIs), it is not easy to employ deep learning in digital pathology. More importantly, computational bottlenecks induced by the gigapixel WSIs make it difficult to use deep learning for end-to-end image representation. To mitigate this challenge, many patch-based approaches have been proposed. Although patching WSIs enables us to use deep learning, we end up with a bag of patches or set representation which makes downstream tasks non-trivial. More importantly, considering set representation per WSI, it is not clear how one can obtain similarity between two WSIs (sets) for tasks like image search matching. To address this challenge, we propose a neural network based on Convolutions Neural Network (CNN) and Deep Sets to learn one permutation invariant vector representation per WSI in an end-to-end manner. Considering available labels at the WSI level - namely, primary site and cancer subtypes - we train the proposed network in a multi-label setting to encode both primary site and diagnosis. Having in mind that every primary site has its own specific cancer subtypes, we propose to use the predicted label for the primary site to recognize the cancer subtype. The proposed architecture is used for transfer learning of WSIs and validated two different tasks, i.e., search and classification. The results show that the proposed architecture can be used to obtain WSI representations that achieve better performance both in terms of retrieval performance and search time against \\emph{Yottixel}, a recently developed search engine for pathology images. Further, the model achieved competitive performance against the state-of-art in lung cancer classification.')
}}
{{ paper('Tailoring automated data augmentation to H&E-stained histopathology',
        'Khrystyna Faryna, Jeroen van der Laak, Geert Litjens',
        openreview='https://openreview.net/forum?id=JrBfXaoxbA2',
        pdf='/proceedings/faryna21.pdf',
        id='I12',
        paper='papers/I12.html',
        proceedings='',
        abstract='Convolutional neural networks (CNN) are sensitive to domain shifts, which can result in poor generalization. In medical imaging, data acquisition conditions differ among institutions, which leads to variations in image properties and thus domain shift. Stain variation in histopathological slides is a prominent example. Data augmentation is one way to make CNNs robust to varying forms of domain shift, but requires extensive hyperparameter tuning. Due to the large search space, this is cumbersome and often leads to sub-optimal generalization performance. In this work, we focus on automated and computationally efficient data augmentation policy selection for histopathological slides. Building upon the RandAugment framework, we introduce several domain-specific modifications relevant to histopathological images, increasing generalizability. We test these modifications on H\\&E-stained histopathology slides from Camelyon17 dataset. Our proposed framework outperforms the state-of-the-art manually engineered data augmentation strategy, achieving an area under the ROC curve of 0.964 compared to 0.958, respectively.')
}}
[% / %]
<a id="shortJ"></a><h3>J1-9 (short): Unsupervised and Representation Learning - 13:45 - 14:30 (UTC+2)</h3>
Chairs: Nikolas Lessmann, Nick Pawlowski <br>
[% .papers %]
{{ paper('Multimodal Generative Learning on the MIMIC-CXR Database',
        'Hendrik J. Klug, Thomas M. Sutter, Julia E Vogt',
        openreview='https://openreview.net/forum?id=ZVqjoKVbYMl',
        pdf='https://openreview.net/pdf?id=ZVqjoKVbYMl',
        id='J1',
        paper='papers/J1.html',
        proceedings='',
        abstract='Machine Learning has become more and more popular in the medical domain over the past years. While supervised machine learning has already been applied successfully, the vast amount of unlabelled data offers new opportunities for un- and self-supervised learning methods. Especially with regard to the multimodal nature of most clinical data, the labelling of multiple data types becomes quickly infeasible in the medical domain. However, to the best of our knowledge, multimodal unsupervised methods have been tested extensively on toy-datasets only but have never been applied to real-world medical data, for direct applications such as disease classification and image generation. In this article, we demonstrate that self-supervised methods provide promising results on medical data while highlighting that the task is extremely challenging and that there is space for substantial improvements.')
}}
{{ paper('TG-DGM: Clustering Brain Activity using a Temporal Graph Deep Generative Model',
        'Simeon Emilov Spasov, Alexander Campbell, Giovana Dimitri, Alessandro Di Stefano, franco scarselli, Pietro Lio',
        openreview='https://openreview.net/forum?id=ULm4D5bsiaE',
        pdf='https://openreview.net/pdf?id=ULm4D5bsiaE',
        id='J2',
        paper='papers/J2.html',
        proceedings='',
        abstract='Spatiotemporal graphs are a natural representation of dynamic brain activity derived from functional magnetic imaging (fMRI) data. Previous works, however, tend to ignore time dynamics of the brain and focus on static graphs. In this paper, we propose a temporal graph deep generative model (TG-DGM) which clusters brain regions into communities that evolve over time. In particular, subject embeddings capture inter-subject variability and its impact on communities using neural networks. We validate our model on the UK Biobank data. Results of up to 0.81 AUC ROC on the task of biological sex classification demonstrate that injecting time dynamics in our model outperforms a static baseline.')
}}
{{ paper('Comparison of Representation Learning Techniques for Tracking in time resolved 3D Ultrasound',
        'Daniel Wulff, Jannis Hagenah, Floris Ernst',
        openreview='https://openreview.net/forum?id=XT40FwD5bV',
        pdf='https://openreview.net/pdf?id=XT40FwD5bV',
        id='J3',
        paper='papers/J3.html',
        proceedings='',
        abstract='3D ultrasound (3DUS) becomes more interesting for target tracking in radiation therapy due to its capability to provide volumetric images in real-time without using ionizing radiation. It is potentially usable for tracking without using fiducials. For this, a method for learning meaningful representations with which recognizing anatomical structures in different time frames is capable would be useful. In this study, 3DUS patches are reduced into a 128-dimensional representation space using conventional autoencoder, variational autoencoder and sliced-wasserstein autoencoder. In the representation space, the capability of separating different ultrasound patches as well as recognizing similar patches is investigated and compared based on a dataset of liver images. Two metrics to evaluate the tracking capability in the representation space are proposed. It is shown that ultrasound patches with different anatomical structures can be distinguished and sets of similar patches can be clustered in representation space. The results indicate that the investigated autoencoders have different levels of usability for target tracking in 3DUS.')
}}
{{ paper('Deep Clustering Activation Maps for Emphysema Subtyping',
        'Weiyi Xie, Colin Jacobs, Bram van Ginneken',
        openreview='https://openreview.net/forum?id=pOFGaVQeXAk',
        pdf='https://openreview.net/pdf?id=pOFGaVQeXAk',
        id='J4',
        paper='papers/J4.html',
        proceedings='',
        abstract='We propose a deep learning clustering method that exploits dense features from a segmentation network for emphysema subtyping from computed tomography (CT) scans. Using dense features enables high-resolution visualization of image regions corresponding to the cluster assignment via dense clustering activation maps (dCAMs). This approach provides model interpretability. We evaluated clustering results on 500 subjects from the COPDGene study, where radiologists manually annotated emphysema sub-types according to their visual CT assessment. We achieved a 43% unsupervised clustering accuracy, outperforming our baseline at 41% and yielding results comparable to supervised classification at 45%. The proposed method also offers a better cluster formation than the baseline, achieving 0.54 in silhouette coefficient and 0.55 in David-Bouldin scores.')
}}
{{ paper('Discrete Pseudohealthy Synthesis: Aortic Root Shape Typification and Type Classification with Pathological Prior',
        'Jannis Hagenah, Floris Ernst',
        openreview='https://openreview.net/forum?id=Fqmbjvawgt',
        pdf='/proceedings/hagenah21.pdf',
        id='J5',
        paper='papers/J5.html',
        proceedings='',
        abstract="In personalized prosthesis shaping, the desired shape remains typically unknown and has to be estimated based on the individual pathological shape. This estimation is also called pseudo healthy synthesis. One example application is the personalization of aortic root prostheses during valve-sparing aortic root surgery. Even though several methods for pseudohealthy synthesis were proposed during the last years, it might not always be necessary to taylor a completely individual and unique prosthesis for each and every patient as this introduces high costs and regulatory issues. Another option is to identify a set of prosthesis types that represents all natural healthy shapes in an adequate way. Then, the pseudohealthy synthesis problem becomes a classification problem, aiming on predicting the optimal prosthesis out of the set of candidates given a pathological shape.In this work, we present a fully automized workflow of unsupervised shape typification and type classification based on pathological data for the example of personalizing aortic root prostheses shapes. We provide a proof-of-concept study on an ex-vivo porcine data set, including a thorough evaluation of the model\\'s hyperparameters and the number of identified shape types. Our study lies the groundwork for a new branch of personalized prosthesis shaping with a high potential of translation to clinical application: Discrete Pseudohealthy Synthesis.")
}}
{{ paper('Improving MRI-based Knee Disorder Diagnosis with Pyramidal Feature Details',
        'Matteo Dunnhofer, Niki Martinel, Christian Micheloni',
        openreview='https://openreview.net/forum?id=7psPmlNffvg',
        pdf='/proceedings/dunnhofer21.pdf',
        id='J6',
        paper='papers/J6.html',
        proceedings='',
        abstract='This paper presents MRPyrNet, a new convolutional neural network (CNN) architecture that improves the capabilities of CNN-based pipelines for knee injury detection via magnetic resonance imaging (MRI). Existing works showed that anomalies are localized in small-sized knee regions that appear in particular areas of MRI scans. Based on such facts, MRPyrNet exploits a Feature Pyramid Network to enhance small appearing features and Pyramidal Detail Pooling to capture such relevant information in a robust way. Experimental results on two publicly available datasets demonstrate that MRPyrNet improves the ACL tear and meniscal tear diagnosis capabilities of two state-of-the-art methodologies. Code is available at https://git.io/JtMPH.')
}}
{{ paper('Membership Inference Attacks on Deep Regression Models for Neuroimaging',
        'Umang Gupta, Dimitris Stripelis, Pradeep K. Lam, Paul Thompson, Jose Luis Ambite, Greg Ver Steeg',
        openreview='https://openreview.net/forum?id=8lL_y9n-CV',
        pdf='/proceedings/gupta21.pdf',
        id='J7',
        paper='papers/J7.html',
        proceedings='',
        abstract="Ensuring the privacy of research participants is vital, even more so in healthcare environments. Deep learning approaches to neuroimaging require large datasets, and this often necessitates sharing data between multiple sites, which is antithetical to the privacy objectives. Federated learning is a commonly proposed solution to this problem. It circumvents the need for data sharing by sharing parameters during the training process. However, we demonstrate that allowing access to parameters may leak private information even if data is never directly shared. In particular, we show that it is possible to infer if a sample was used to train the model given only access to the model prediction (black-box) or access to the model itself (white-box) and some leaked samples from the training data distribution. Such attacks are commonly referred to as \\textit{Membership Inference attacks}. We show realistic Membership Inference attacks on deep learning models trained for 3D neuroimaging tasks in a centralized as well as decentralized setup. We demonstrate feasible attacks on brain age prediction models (deep learning models that predict a person\\'s age from their brain MRI scan). We correctly identified whether an MRI scan was used in model training with a 60% to over 80% success rate depending on model complexity and security assumptions.")
}}
{{ paper('Guided Filter Regularization for Improved Disentanglement of Shape and Appearance in Diffeomorphic Autoencoders',
        'Hristina Uzunova, Heinz Handels, Jan Ehrhardt',
        openreview='https://openreview.net/forum?id=ILEMHPV_Lc2',
        pdf='/proceedings/uzunova21.pdf',
        id='J8',
        paper='papers/J8.html',
        proceedings='',
        abstract='Diffeomorphic and deforming autoencoders have been recently explored in the field of medical imaging for appearance and  shape disentanglement. Both models are based on the deformable template paradigm, however they show different weaknesses for the representation of medical images. Diffeomorphic autoencoders only consider spatial deformations, whereas deforming autoencoders also  regard changes in the appearance, however no uniform template is generated for the whole training dataset, and the appearance is modeled depending on a very few parameters. In this work, we propose a method that represents images based on a global template, where next to the  spatial displacement, the appearance is modeled as the pixel-wise intensity difference to the unified template. To however ensure that the generated appearance offsets adhere to the template shape,  a guided filter smoothing of the appearance map is integrated into an end-to-end training process. This regularization significantly improves the disentanglement of shape and appearance and thus enables multi-modal image modeling. Furthermore, the generated templates are crisper and the registration accuracy improves. Our experiments also show applications of the proposed approach in the field of automatic population analysis. ')
}}
{{ paper('Self-supervised Out-of-distribution Detection for Cardiac CMR Segmentation',
        'Camila Gonzalez, Anirban Mukhopadhyay',
        openreview='https://openreview.net/forum?id=E5CpgfwHBoC',
        pdf='/proceedings/gonzalez21.pdf',
        id='J9',
        paper='papers/J9.html',
        proceedings='',
        abstract='The segmentation of cardiac structures in Cine Magnetic Resonance imaging (CMR) plays an important role in monitoring ventricular function, and many deep learning solutions have been introduced that successfully automate this task. Yet due to variabilities in the CMR acquisition process, images from different centers or acquisition protocols differ considerably. This causes deep learning models to fail silently. It is therefore crucial to identify out-of-distribution (OOD) samples for which the trained model is unsuitable. For models with a self-supervised proxy task, we propose a simple method to identify OOD samples that does not require adapting the model architecture or access to a separate OOD dataset during training. As the performance of self-supervised tasks can be assessed without ground truth information, it indicates during test time when a sample differs from the training distribution. The proposed method combines a voxel-wise uncertainty estimate with the self-supervision information. Our approach is validated across three CMR datasets and two different proxy tasks. We find that it is more effective at detecting OOD samples than state-of-the-art post-hoc OOD detection and uncertainty estimation approaches.')
}}
[% / %]
<a id="longL"></a><h3>L1-3 (long): Learning with Noisy Labels and Limited Data - 16:00 - 16:30 (UTC+2)</h3>
Chairs: Geert Litjens, Ozan Oktay <br>
[% .papers %]
{{ paper('Untangling the Small Intestine in 3D cine-MRI using Deep Stochastic Tracking',
        'Louis van Harten, Catharina de Jonge, Jaap Stoker, Ivana Isgum',
        openreview='https://openreview.net/forum?id=cfYAFR6s6iJ',
        pdf='/proceedings/vanharten21.pdf',
        id='L1',
        paper='papers/L1.html',
        proceedings='',
        abstract='Motility of the small intestine is a valuable metric in the evaluation of gastrointestinal disorders. Cine-MRI of the abdomen is a non-invasive imaging technique allowing evaluation of this motility. While 2D cine-MR imaging is increasingly used for this purpose in both clinical practice and in research settings, the potential of 3D cine-MR imaging has been largely underexplored. In the absence of image analysis tools enabling investigation of the intestines as 3D structures, the assessment of motility in 3D cine-images is generally limited to the evaluation of movement in separate 2D slices. Hence, to obtain an untangled representation of the small intestine in 3D cine-MRI, we propose a method to extract a centerline of the intestine, thereby allowing easier (visual) assessment by human observers, as well as providing a possible starting point for automatic analysis methods quantifying peristaltic bowel movement along intestinal segments. The proposed method automatically tracks individual sections of the small intestine in 3D space, using a stochastic tracker built on top of a CNN-based orientation classifier. We show that the proposed method outperforms a non-stochastic iterative tracking approach.')
}}
{{ paper('M-GCN: A Multimodal Graph Convolutional Network to Integrate Functional and Structural Connectomics Data to Predict Multidimensional Phenotypic Characterizations',
        'Niharika Shimona Dsouza, Mary Beth Nebel, Deana Crocetti, Joshua Robinson, Stewart Mostofsky, Archana Venkataraman',
        openreview='https://openreview.net/forum?id=ud-iBiED9zb',
        pdf='/proceedings/dsouza21.pdf',
        id='L2',
        paper='papers/L2.html',
        proceedings='',
        abstract='We propose a multimodal graph convolutional network (M-GCN) that integrates resting-state fMRI connectivity and diffusion tensor imaging tractography to predict phenotypic measures. Our specialized M-GCN filters act topologically on the functional connectivity matrices, as guided by the subject-wise structural connectomes. The inclusion of structural information also acts as a regularizer and helps extract rich data embeddings that are predictive of clinical outcomes. We validate our framework on 275 healthy individuals from the Human Connectome Project and 57 individuals diagnosed with Autism Spectrum Disorder from an in-house data to predict cognitive measures and behavioral deficits respectively. We demonstrate that the M-GCN outperforms several state-of-the-art baselines in a five-fold cross validated setting and extracts predictive biomarkers from both healthy and autistic populations. Our framework thus provides the representational flexibility to exploit the complementary nature of structure and function and map this information to phenotypic measures in the presence of limited training data.')
}}
{{ paper('Improved model-based deep learning for quantitative susceptibility mapping',
        'JUAN LIU',
        openreview='https://openreview.net/forum?id=Y7koM_09Cme',
        pdf='/proceedings/liu21a.pdf',
        id='L3',
        paper='papers/L3.html',
        proceedings='',
        abstract='Quantitative susceptibility mapping (QSM) is a magnetic resonance imaging (MRI) technique that estimates magnetic susceptibility of tissue from MR phase measurements. Recently, several supervised deep learning (DL) techniques have demonstrated impressive performance in solving the challenging ill-posed field-to-source inverse QSM reconstruction problem. To address the lack of the inherent non-existent ground-truth QSM references, a model-based method was recently proposed using the well-established physical model. However, it fails to perform well at the regions with large susceptibility variations. Here, we proposed uQSM+ with data augmentation techniques to improve the model-based learning. The proposed method was evaluated on a multi-orientation QSM datasets and 2019 QSM reconstruction challenge datasets. Quantitative and qualitative evaluation showed that uQSM+ and zero-shot uQSM+ was capable of reconstructing high quality QSM. The code is available at \\inkhttps{https://github.com/juana313/uQSM-plus}.')
}}
[% / %]
<a id="shortK"></a><h3>K1-9 (short): Learning with Noisy Labels and Limited Data - 16:45 - 17:30 (UTC+2)</h3>
Chairs: Hoel Kervadec, Max-Heinrich Laves <br>
[% .papers %]
{{ paper('Semi-Supervised Siamese Network for Identifying Bad Data in Medical Imaging Datasets',
        'Niamh Belton, Kathleen M Curran, Aonghus Lawlor',
        openreview='https://openreview.net/forum?id=0bpkIn63sNG',
        pdf='https://openreview.net/pdf?id=0bpkIn63sNG',
        id='K1',
        paper='papers/K1.html',
        proceedings='',
        abstract="Noisy data present in medical imaging datasets can often aid the development of robust models that are equipped to handle real-world data. However, if the bad data contains insufficient anatomical information, it can have a severe negative effect on the model\\'s performance. We propose a novel methodology using a semi-supervised Siamese network to identify bad data. This method requires only a small pool of \\'reference\\' medical images to be reviewed by a non-expert human to ensure the major anatomical structures are present in the Field of View. The model trains on this reference set and identifies bad data by using the Siamese network to compute the distance between the reference set and all other medical images in the dataset. This methodology achieves an Area Under the Curve (AUC) of 0.989 for identifying bad data. Code will be available at https://git.io/JYFuV.")
}}
{{ paper('mGEV: Extension of the GEV Activation to Multiclass Classification',
        'Joshua Thomas Bridge, Yalin Zheng',
        openreview='https://openreview.net/forum?id=rKiYUGvII6',
        pdf='https://openreview.net/pdf?id=rKiYUGvII6',
        id='K2',
        paper='papers/K2.html',
        proceedings='',
        abstract='Unbalanced data poses a challenge when training machine learning algorithms; the algorithm often overfits on the dominant class and neglects the smaller classes. While methods such as oversampling aim to rebalance the data, this can lead to overfitting. When a certain class is underrepresented, either because it a rare disease or few images exist then methods are needed which can adequately account for this. The generalized extreme value (GEV) activation has recently been proposed as a solution to highly unbalanced data; however, the GEV activation is only available for binary classification. We extend this to the multiclass case with the multiclass GEV (mGEV) activation. We conduct experiments on X-ray images, with three classes, showing much-improved performance over the commonly used softmax activation. Code for the mGEV activation is available at [https://github.com/JTBridge/GEV].')
}}
{{ paper('Weakly supervised 3D ConvLSTMs for high precision Monte-Carlo radiotherapy dose simulations',
        'Sonia Martinot, Norbert Bus, Maria Vakalopoulou, charlotte robert, Eric Deutsch, Nikos Paragios',
        openreview='https://openreview.net/forum?id=V4k0rNW7IG-',
        pdf='https://openreview.net/pdf?id=V4k0rNW7IG-',
        id='K3',
        paper='papers/K3.html',
        proceedings='',
        abstract='Radiotherapy dose simulation using the Monte-Carlo technique surpasses existing algorithms in terms of precision but remains too time-consuming to be integrated in clinical workflows. We introduce a 3D recurrent and fully convolutional neural network architecture to produce high-precision Monte-Carlo-like dose simulations from low-precision and cheap-to-compute ones. We use the noise-to-noise setting, a weakly supervised training strategy, by training the models solely on low-precision data without expensive-to-compute, high-precision dose simulations. Several evaluation metrics are used to compare with other methods and to assess the clinical viability and quality of the generated dose maps.')
}}
{{ paper('DS6, Deformation-aware Semi-supervised Learning: Application to Small Vessel Segmentation with Noisy Training Data',
        'Soumick Chatterjee, Kartik Prabhu, Mahantesh Pattadkal, Gerda Bortsova, Chompunuch Sarasaen, Florian Dubost, Hendrik Mattern, Marleen de Bruijne, Oliver Speck, Andreas Nürnberger',
        openreview='https://openreview.net/forum?id=2t0_AxD1otB',
        pdf='https://openreview.net/pdf?id=2t0_AxD1otB',
        id='K4',
        paper='papers/K4.html',
        proceedings='',
        abstract='The advancement of 7 Tesla MRI systems enabled the depiction of very small vessels in the brain. Segmentation and quantification of the small vessels in the brain is a critical step in the study of Cerebral Small Vessel Disease, which is a challenging task. This paper proposes a deep learning based on U-Net Multi-Scale Supervision architecture to automatically segment small vessels in 7 Tesla 3D Time-of-Flight (TOF) Magnetic Resonance Angiography (MRA) data trained on a small imperfect semi-automatically segmented dataset and was made equivariant to elastic deformations in a self-supervised manner using deformation-aware learning to improve the generalisation performance. The proposed method achieved a dice score of 80.44 +/- 0.83 while being compared against the semi-automatically created labels and 62.07 while comparing against manually segmented region. ')
}}
{{ paper('Deep ensemble model for segmenting microscopy images in the presence of limited labeled data',
        'Jan Mikolaj Kaminski, Ilary Allodi, Roser Montañana-Rosell, Raghavendra Selvan, Ole Kiehn',
        openreview='https://openreview.net/forum?id=PLSdnHPx-W6',
        pdf='https://openreview.net/pdf?id=PLSdnHPx-W6',
        id='K5',
        paper='papers/K5.html',
        proceedings='',
        abstract='Obtaining large amounts of high quality labeled microscopy data is expensive and time-consuming. To overcome this issue, we propose a deep ensemble model which aims to utilise limited labeled training data. We train multiple identical Convolutional Neural Network (CNN) segmentation models on training data that is partitioned into folds in two steps. First, the data is split based on sample diversity or expert knowledge reflecting the possible {\\em modes} of the underlying data distribution. In the second step, these partitions are split into random folds like in a cross-validation setting. Segmentation models based on the U-net architecture are trained on each of these resulting folds yielding the candidate models for our deep ensemble model which are aggregated to obtain the final prediction. The proposed deep ensemble model is compared to relevant baselines, in their ability to segment interneurons in microscopic images of mice spinal cord, showing improved performance on an independent test set.')
}}
{{ paper('Learning the Latent Heat Diffusion Process through Structural Brain Network from Longitudinal β-Amyloid Data',
        'Md Asadullah Turja, Guorong Wu, Defu Yang, Martin Andreas Styner',
        openreview='https://openreview.net/forum?id=S3QYCe74DPu',
        pdf='/proceedings/turja21.pdf',
        id='K6',
        paper='papers/K6.html',
        proceedings='',
        abstract="The excessive deposition of misfolded proteins such as amyloid-β~(Aβ) protein is an aging event underlying several neurodegenerative diseases. Mounting evidence shows that the spreading of neuropathological burden has a strong association to the white matter tracts in the brain which can be measured using diffusion-weighted imaging and tractography technologies. Most of the previous studies analyze the dynamic progression of amyloid using cross-sectional data which is not robust to the heterogeneous Aβ dynamics across the population. In this regard, we propose a graph neural network-based learning framework to capture the disease-related dynamics by tracking the spreading of amyloid across brain networks from the subject-specific longitudinal PET images. To learn from limited (2 – 3 timestamps) and noisy longitudinal data, we restrict the space of amyloid propagation patterns to a latent heat diffusion model which is constrained by the anatomical connectivity of the brain. Our experiments show that restricting the dynamics to be a heat diffusion mechanism helps to train a robust deep neural network for predicting future time points and classifying Alzheimer\\'s disease brain.")
}}
{{ paper('Attention via Scattering Transforms for Segmentation of Small Intravascular Ultrasound Data Sets',
        'Lennart Bargsten, Katharina A. Riedl, Tobias Wissel, Fabian J. Brunner, Klaus Schaefers, Michael Grass, Stefan Blankenberg, Moritz Seiffert, Alexander Schlaefer',
        openreview='https://openreview.net/forum?id=GDs7V3mS1h9',
        pdf='/proceedings/bargsten21.pdf',
        id='K7',
        paper='papers/K7.html',
        proceedings='',
        abstract='Using intracoronary imaging modalities like intravascular ultrasound (IVUS) has a positive impact on the results of percutaneous coronary interventions. Efficient extraction of important vessel metrics like lumen diameter, vessel wall thickness or plaque burden via automatic segmentation of IVUS images can improve the clinical workflow. State-of-the-art segmentation results are usually achieved by data-driven methods like convolutional neural networks (CNNs). However, clinical data sets are often rather small leading to extraction of image features which are not very meaningful and thus decreasing performance. This is also the case for some applications which inherently allow for only small amounts of available data, e.g., detection of diseases with extremely small prevalence or online-adaptation of an existing algorithm to individual patients.In this work we investigate how integrating scattering transformations - as special forms of wavelet transformations - into CNNs could improve the extraction of meaningful features. To this end, we developed a novel network module which uses features of a scattering transform for an attention mechanism.We observed that this approach improves the results of calcium segmentation up to 8.2 % (relatively) in terms of the Dice coefficient and 24.8 % in terms of the modified Hausdorff distance. In the case of lumen and vessel wall segmentation, the improvements are up to 2.3 % (relatively) in terms of the Dice coefficient and 30.8 % in terms of the modified Hausdorff distance.Incorporating scattering transformations as a component of an attention block into CNNs improves the segmentation results on small IVUS segmentation data sets. In general, scattering transformations can help in situations where efficient feature extractors can not be learned via the training data. This makes our attention module an interesting candidate for applications like few-shot learning for patient adaptation or detection of rare diseases.')
}}
{{ paper('Learning Interclass Relations for Intravenous Contrast Phase Classification in CT',
        'Raouf Muhamedrahimov, Amir Bar, Ayelet Akselrod-Ballin',
        openreview='https://openreview.net/forum?id=B01pd5ot0w6',
        pdf='/proceedings/muhamedrahimov21.pdf',
        id='K8',
        paper='papers/K8.html',
        proceedings='',
        abstract='In classification, categories are typically treated as independent of one-another. In many problems, however, this neglects the natural relations that exist between categories, which are often dictated by an underlying biological or physical process. In this work, we propose novel formulations of the classification problem, aimed at reintroducing class relations into the training process. We demonstrate the benefit of these approaches for the classification of intravenous contrast enhancement phase in CT images, an important task in the medical imaging domain. First, we propose manual ways reintroduce knowledge about problem-specific interclass relations into the training process. Second, we propose a general approach to jointly learn categorical label representations that can implicitly encode natural interclass relations, alleviating the need for strong prior assumptions or knowledge. We show that these improvements are most significant for smaller training sets, typical in the medical imaging domain where access to large amounts of labelled data is often not trivial.')
}}
{{ paper('Improving Weakly Supervised Lesion Segmentation using Multi-Task Learning',
        'Tianshu Chu, Xinmeng Li, Huy V. Vo, Ronald M. Summers, Elena Sizikova',
        openreview='https://openreview.net/forum?id=-9bAYexxLtN',
        pdf='/proceedings/chuli21.pdf',
        id='K9',
        paper='papers/K9.html',
        proceedings='',
        abstract="We introduce the concept of multi-task learning to weakly-supervised lesion segmentation, one of the most critical and challenging tasks in medical imaging. Due to the lesions\\' heterogeneous nature, it is difficult for machine learning models to capture the corresponding variability. We propose to jointly train a lesion segmentation model and a lesion classifier in a multi-task learning fashion, where the supervision of the latter is obtained by clustering the RECIST measurements of the lesions. We evaluate our approach specifically on liver lesion segmentation and more generally on lesion segmentation in computed tomography (CT), as well as segmentation of skin lesions from dermatoscopic images. We show that the proposed joint training improves the quality of the lesion segmentation by 4% percent according to the Dice coefficient and 6% according to averaged Hausdorff distance (AVD), while reducing the training time required by up to 75%. ")
}}
[% / %]
<a id="shortL"></a><h3>L4-9 (short): Detection and Diagnosis 2 - 16:45 - 17:30 (UTC+2)</h3>
Chairs: Christian Baumgartner, Colin Jacobs <br>
[% .papers %]
{{ paper('Prediction of Ki67 scores from H&E stained breast cancer sections using convolutional neural networks',
        'Philippe Weitz, Balazs Acs, Johan Hartman, Mattias Rantalainen',
        openreview='https://openreview.net/forum?id=W9sz0zHk33h',
        pdf='https://openreview.net/pdf?id=W9sz0zHk33h',
        id='L4',
        paper='papers/L4.html',
        proceedings='',
        abstract='Ki67 is an established marker of proliferation in breast cancer, but currently has limited clinical value due to limitations of the analytical validity of immunohistochemistry (IHC) -based Ki67 scoring. While the inter-assessor variability of scoring can be improved through image analysis software, Ki67 IHC also suffers from a lack of standardized staining protocols and is not part of routine pathology workflow in most countries. This could potentially be alleviated through directly predicting Ki67 scores from routine hematoxylin and eosin (H\\&E) stained whole-slide-images (WSIs). We compared four different deep learning based approaches to  predict Ki67 scores from routine H\\&E stained WSIs in a dataset that consists of matched H\\&E and Ki67 WSIs from 126 breast cancer patients, resulting in a Spearman correlation between WSI cancer ROI averages of 0.546 for the best performing model in a 5-fold cross-validation (CV). These findings suggest that it is possible to predict the Ki67 score from H\\&E stained WSIs, but validation in a larger cohort is required to meaningfully distinguish the performance of the methods that were investigated. ')
}}
{{ paper('Feedback Graph Attention Convolutional Network for MR Images Enhancement by Exploring Self-Similarity Features',
        'Xiaobin Hu, Yanyang Yan, Wenqi Ren, Hongwei Li, Amirhossein Bayat, yu zhao, bjoern menze',
        openreview='https://openreview.net/forum?id=k1BSWQqHoMV',
        pdf='/proceedings/hu21.pdf',
        id='L5',
        paper='papers/L5.html',
        proceedings='',
        abstract='Artifacts, blur, and noise are the common distortions degrading MRI images during the acquisition process, and deep neural networks have been demonstrated to help in improving image quality. To well exploit global structural information and self-similarity details, we propose a novel MR image enhancement network, named Feedback Graph Attention Convolutional Network (FB-GACN).As a key innovation, we consider the global structure of an image by building a graph network from image sub-regions that we consider to be node features, linking them non-locally according to their similarity. The proposed model consists of three main parts:1) The parallel graph similarity branch and content branch, where the graph similarity branch aims at exploiting the similarity and symmetry across different image sub-regions in low-resolution feature space and provides additional priors for the content branch to enhance texture details.2) A feedback mechanism with a recurrent structure to refine low-level representations with high-level information and generate powerful high-level texture details by handling the feedback connections. 3) A reconstruction to remove the artifacts and recover super-resolution images by using the estimated sub-region self-similarity priors obtained from the graph similarity branch. We evaluate our method on two image enhancement tasks: i) cross-protocol super resolution of diffusion MRI; ii) artifact removal of FLAIR MR images. Experimental results demonstrate that the proposed algorithm outperforms the state-of-the-art methods.')
}}
{{ paper('Unifying Brain Age Prediction and Age-Conditioned Template Generation with a Deterministic Autoencoder',
        'Pauline Mouches, Matthias Wilms, Deepthi Rajashekar, Sonke Langner, Nils Forkert',
        openreview='https://openreview.net/forum?id=9ClUQ2ELJap',
        pdf='/proceedings/mouches21.pdf',
        id='L6',
        paper='papers/L6.html',
        proceedings='',
        abstract='Age-related morphological brain changes are known to be different in healthy and disease-affected aging. Biological brain age estimation from MRI scans is a common way to quantify this effect whereas differences between biological and chronological age indicate degenerative processes. The ability to visualize and analyze the morphological age-related changes in the image space directly is essential to improve the understanding of brain aging. In this work, we propose a novel deep learning based approach to unify biological brain age estimation and age-conditioned template creation in a single, consistent model. We achieve this by developing a deterministic autoencoder that successfully disentangles age-related morphological changes and subject-specific variations. This allows its use as a brain age regressor as well as a generative brain aging model. The proposed approach demonstrates accurate biological brain age prediction, and realistic generation of age-conditioned brain templates and simulated age-specific brain images when applied to a database of more than 2000 subjects.')
}}
{{ paper('GOAL: Gist-set Online Active Learning for Efficient Chest X-ray Image Annotation',
        'Chanh Nguyen, Minh Thanh Huynh, Minh Quan Tran, Ngoc Hoang Nguyen, Mudit Jain, Van Doan Ngo, Tan Duc Vo, Trung Bui, Steven Quoc Hung Truong',
        openreview='https://openreview.net/forum?id=boTEEpM8mu',
        pdf='/proceedings/nguyen21.pdf',
        id='L7',
        paper='papers/L7.html',
        proceedings='',
        abstract='Deep learning in medical image analysis often requires an extensive amount of high-quality labeled data for training to achieve Human-level accuracy. We propose Gist-set Online Active Learning (GOAL), a novel solution for limited high-quality labeled data in medical imaging analysis. Our approach advances the existing active learning methods in three aspects. Firstly, we improve the classification performance with fewer manual annotations by presenting a sample selection strategy called gist set selection. Secondly, unlike traditional methods focusing only on random uncertain samples of low prediction confidence, we propose a new method in which only informative uncertain samples are selected for human annotation. Thirdly, we propose an application of online learning where high-confidence samples are automatically selected, iteratively assigned, and pseudo-labels are updated. We validated our approach on two private and one public dataset. The experimental results show that, by applying GOAL, we can reduce required labeled data up to 88% while maintaining the same F1 scores compared to the models trained on full datasets')
}}
{{ paper('EPIC-Survival: End-to-end Part Inferred Clustering for Survival Analysis, with Prognostic Stratification Boosting',
        'Hassan Muhammad, Chensu Xie, Carlie S Sigel, Michael Doukas, Lindsay Alpert, Amber Lea Simpson, Thomas J Fuchs',
        openreview='https://openreview.net/forum?id=JSSwHS_GU63',
        pdf='/proceedings/muhammad21.pdf',
        id='L8',
        paper='papers/L8.html',
        proceedings='',
        abstract='Histopathology-based survival modelling has two major hurdles. Firstly, a well-performing survival model has minimal clinical application if it does not contribute to the stratification of a cancer patient cohort into different risk groups, preferably driven by histologic morphologies. In the clinical setting, individuals are not given specific prognostic predictions, but are rather predicted to lie within a risk group which has a general survival trend. Thus, It is imperative that a survival model produces well-stratified risk groups. Secondly, until now, survival modelling was done in a two-stage approach (encoding and aggregation). EPIC-Survival bridges encoding and aggregation into an end-to-end survival modelling approach, while introducing stratification boosting to encourage the model to not only optimize ranking, but also to discriminate between risk groups. In this study we show that EPIC-Survival performs better than other approaches in modelling intrahepatic cholangiocarcinoma (ICC), a historically difficult cancer to model. We found that stratification boosting further improves model performance and helps identify specific histologic differences, not commonly sought out in ICC.')
}}
{{ paper('CheXseg: Combining Expert Annotations with DNN-generated Saliency Maps for X-ray Segmentation',
        'Soham Uday Gadgil, Mark Endo, Emily Wen, Andrew Y. Ng, Pranav Rajpurkar',
        openreview='https://openreview.net/forum?id=eA7PGMYmHFA',
        pdf='/proceedings/gadgil21.pdf',
        id='L9',
        paper='papers/L9.html',
        proceedings='',
        abstract='Medical image segmentation models are typically supervised by expert annotations at the pixel-level, which can be expensive to acquire. In this work, we propose a method that combines the high quality of pixel-level expert annotations with the scale of coarse DNN-generated saliency maps for training multi-label semantic segmentation models. We demonstrate the application of our semi-supervised method, which we call CheXseg, on multi-label chest X-ray interpretation. We find that CheXseg improves upon the performance (mIoU) of fully-supervised methods that use only pixel-level expert annotations by 9.7% and weakly-supervised methods that use only DNN-generated saliency maps by 73.1%. Our best method is able to match radiologist agreement on three out of ten pathologies and reduces the overall performance gap by 57.2% as compared to weakly-supervised methods.')
}}
[% / %]
