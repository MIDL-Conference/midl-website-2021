---
title: "Program at a glance"
---

# Program at a glance

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


<tr><th id='t01' class='col1' >06:15</th><th id='t01' class='col2'>9:15</th><th id='r00' class='col3'>15:15</th><th id='t01' class='col4'>21:15</th><th colspan='2' id='ckeynote'><div><a href="https://youtu.be/lK9IIW9GcPw" style='color:white'>Keynote - Polina Golland</a></div></th><th colspan='2' id='ckeynote'><div><a href="https://youtu.be/lXBIBS-2iBk" style='color:white'>Keynote - Bernhard Schölkopf</a></div></th><th colspan='2' id='ckeynote_r'><div><a href="https://youtu.be/XiAbR8Nt_is" style='color:white'>Keynote - Bernd Stahl</a></div></th>




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

### Legend

<table>
<tr><th id='clong_v'><div id="title_legend">Long Videos</div></th><th><div id="text_legend">Passive viewing of long oral videos (10-13 minutes each).<br> Questions in chat are collected for later live discussion.</div></th>
    <tr><th id='clong'><div id="title_legend">Long Oral Discussion</div></th><th><div id="text_legend"><b>(max.) 3</b> minute introduction of each speaker/paper<br> followed by 21 minute discussion (group of 3)</div></th>
<tr><th id='cshort_v'><div id="title_legend">Short Videos</div></th><th><div id="text_legend">Passive viewing of short oral videos (4-6 minutes each).<br> Dual Track. Questions in chat are collected for later live discussion.</div></th>
<tr><th id='cshort'><div id="title_legend">Short Oral Discussion</div></th><th><div id="text_legend">Split into three consecutive groups of 3. <b>(max.) 90 second</b> introduction<br> of each speaker/paper followed by 10.5 minute discussion (group of 3). Dual Track.</div></th>
    <tr><th id='cposter'><div id="title_legend">Individual Poster Rooms</div></th><th><div id="text_legend">Virtual poster session in GatherTown (all papers of preceeding sessions)<br> Preview of poster PDF (slide) and ad-hoc video chat with presenters (other attendees) </div></th>
<tr><th id='ckeynote'><div id="title_legend">Keynote</div></th><th><div id="text_legend">Live (virtual) presentation with following discussion in Webinar. </div></th>

<tr><th id='cspecial'><div id="title_legend">Industry and Sponsors</div></th><th><div id="text_legend">Virtual booth and videos presenting supporting companies.<br>Networking and career opportunities. </div></th>
<tr><th id='cmentor'><div id="title_legend">Study Groups / Mentors</div></th><th><div id="text_legend">(optional with prior sign-up: <a href="https://forms.gle/CNPTBZQ4fzWuFKY6A">Google Form</a>). Study groups assemble questions<br> for live discussion. Meet in dedicated study rooms and also get great advice from mentors. </div></th>
<tr><th id='cbreak'><div id="title_legend">Breaks: GatherTown</div></th><th><div id="text_legend">Meet new and old colleagues for ad-hoc (video) chats on the hallway<br>or in free meeting spaces. Have coffee or enjoy views over L&uuml;beck.</div></th></tr>
</table>

---

Since the program of this years MIDL might appear quite differently from what you expect, there is a [video](https://youtu.be/Nlzt1LgOubc) explaining how you can enjoy the scientific presentations and discussions throughout the conference!

We gave our best to give every participant the opportunity for live interaction with the authors, regardless of the timezone. Therefore, each conference day is divided into two parts: The active part and the passive part.
The active part - the <b>prime time</b> - takes place in the time frame that is most convenient across all time zones and is marked in yellow.

During this active part, live spotlight presentations of and discussions with the authors of all accepted papers are scheduled. Additionally, the keynotes, virtual poster sessions as well as social events will take place during the active phase. Hence, participants from all over the world get the chance to discuss the presented research, meet new colleagues and old friends, and enjoy a live virtual event.

In the passive part, the full presentation videos of all accepted papers are shown in moderated sessions. Each presentation is streamed twice to address the different time zones, once the day before after the active phase and once right before the active phase where the paper is discussed. Questions that arise during these sessions will be collected and answered in the corresponding discussion session during the active phase. All presentation videos will also be accessible on the homepage so that they can also be enjoyed outside the moderated sessions.

---

## Important dates

All deadlines are at 23:59, [UTC -12](https://www.timeanddate.com/time/map/) ([AoE](https://en.wikipedia.org/wiki/Anywhere_on_Earth) timezone).

[% .deadlines %]
### Full Papers
* **<s>Paper registration open</s>** <s>1 January 2021</s>
* **<s>Paper registration deadline</s>** <s>10 February 2021</s>
* **<s>Paper submission deadline</s>** <s>17 February 2021</s>
* **<s>Reviews available</s>** <s>10 March 2021</s>
* **<s>Rebuttal / discussion period</s>** <s>10 March to 22 March 2021</s>
* **<s>Rebuttals due</s>** <s>17 March 2021</s>
* **<s>Discussion phase</s>** <s>18 to 22 March 2021</s>
* **<s>Notification of acceptance</s>** <s>31 March 2021</s>
* **<s>Deadline for uploading videos</s>** <s>28 June 20201</s>

### Short Papers
* **<s>Paper registration open</s>** <s>1 January 2021</s>
* **<s>Paper registration deadline</s>** <s>6 April 2021</s> <s>9 April 2021</s>
* **<s>Paper submission deadline</s>** <s>13 April 2021</s>
* **<s>Notification of acceptance</s>** <s>12 May 2021</s>

### Doctoral Symposium
* **<s>Application deadline</s>** <s>4 June 2021</s>
* **<s>Notification of acceptance</s>** <s>14 June 2021</s>
* **<s>Doctoral Symposium</s>** <s>2 July 2021</s>

### Conference dates
* [**<s>Doctoral Symposium</s>**](/doctoral-symposium.html) <s>2 July 2021</s>
* [**<s>MIDL 2021</s>**](/program.html) <s>7-9 July 2021</s>

### MedIA Special Issue
* **<s>Paper submission deadline</s>** <s>August 2021</s>
* **Publication** January/February 2022 (if no major revisions are required)

[% / %]

---

## iCalendar
An online iCalendar with all dates and schedule is [available](https://www.rob.uni-luebeck.de/midl2021_cal/MIDL%202021.ics).
It can conveniently be subscribed to and integrated in many calendar applications:

* [Google Calendar](https://support.google.com/calendar/answer/37100?hl=en&co=GENIE.Platform=Desktop)
* [Thunderbird](https://support.mozilla.org/en-US/kb/creating-new-calendars#w_icalendar-ics)
* [Apple Calendar](https://support.apple.com/guide/calendar/subscribe-to-calendars-icl1022/mac)
