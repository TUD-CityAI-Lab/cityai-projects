---
layout: default
title: "Listening to our Cities: Using Smart Sensors and Machine Learning to Study Urban Noise Pollution"
---

<ul class="nav project-nav col-12 col-lg-auto me-lg-auto mb-2">
  <li><a href="#contact" class="nav-link px-2">Contact</a></li>
</ul>

## Listening to our Cities: Using Smart Sensors and Machine Learning to Study Urban Noise Pollution

The sound of urban environments is often dominated by noise from transportation and residents, with profound effects on health and wellbeing. Higher noise exposure has been correlated with higher stress levels, sleep disruptions and cardiovascular diseases. In order to understand and mitigate noise pollution in the urban environment, sophisticated information on the local soundscape is neccessary. Current noise mapping efforts are often based on averaged sound levels for day, evening, and night time. While such aggregations are widely available and simplify noise mapping, they do not capture many aspects of the human perception of noise. For example, a constant background noise may have different effects than high-peak noise events, yet both could result in the same averaged sound level. Furthermore, such measures only account for the perceived loudness, but ignore other aspects of the human perception of sound. 

The goal of this project is to develop techniques for holistic noise maps, which takes into account how we as humans perceive urban noise. For this purpose, we developed our own soundscape sensor and successfully deployed a total of more than 50 sensors in Amsterdam and Delft.

![Noise mapping with smart sensors]({{ 'noise-pollution-and-perception/images/sensor_noise_mapping.jpg' | relative_url }})

### Urban soundscape sensor
The sensor measures not only how loud the environment is, but also predicts what causes the sound. It detects for example traffic noise, crowd noises, emergency sirens, but also pleasant sounds such as bird song. All audio is processed on the device itself, which means no audio is recorded or transmitted. This privacy-first approach is important for a deployment in urban areas. 

The sensor is power autonomous thanks to an integrated solar panel and backup battery. For many other sensors, municipalities have to hire electricians to connect sensors to power from light poles, resulting in additional work, cost, and administrative processes. As our sensor is intended for research deployments, the self-sufficient power design facilitates deployments of larger scales. The sensor supports data logging to a MicroSD card and can be connected to LoRaWAN for wireless transmittion of aggrefated soundscape metrics. 

<div class="row">
  <div class="col-sm-12" style='text-align: center'>
    <img src="{{ 'noise-pollution-and-perception/images/sensor-diagram.png' | relative_url }}" style="max-height: 330pt; border: 1px solid black;">
  </div>
</div>

<br>

The hardare and firmware are currently in review to be published as open hardware. This allows other researchers to reproduce these sensors for their own noise monitoring purposes. Future updates of the sensor may include models to predict soundscape attributes, which indicate e.g., how lively or pleasant a sound environment is perceived by people.

<div class="row">
  <div class="col-sm-6" style='text-align: center'>
    <img src="{{ 'noise-pollution-and-perception/images/sensor-terrace-1.webp' | relative_url }}" style="max-height: 330pt">
  </div>
  <div class="col-sm-6" style='text-align: center'>
    <img src="{{ 'noise-pollution-and-perception/images/sensor_board.webp' | relative_url }}" style="max-height: 330pt">
  </div>
</div>

<br>

## Citizen science soundscape sensor deployment in Delft
In Summer 2025, we deployed 39 soundscape sensors in and around Delft with the help of residents willing to install such a sensor at their home. The sensors where deployed for several weeks before we collected them to analyze the collected noise data. We are now in the process of analyzing this data.


<div class="row">
  <div class="col-sm-4" style='text-align: center; margin-bottom: 5pt;'>
    <img src="{{ 'noise-pollution-and-perception/images/delft-1.webp' | relative_url }}" style="max-height: 330pt">
  </div>
  <div class="col-sm-4" style='text-align: center; margin-bottom: 5pt;'>
    <img src="{{ 'noise-pollution-and-perception/images/delft-2.webp' | relative_url }}" style="max-height: 330pt">
  </div>
  <div class="col-sm-4" style='text-align: center;'>
    <img src="{{ 'noise-pollution-and-perception/images/deploying-sensor.webp' | relative_url }}" style="max-height: 330pt">
  </div>
</div>

<hr>

Some first (preliminary results) show when birds are most audible. These predictions match our expectations as birds are generally most audible in the early morning, which matches the sensor detections. Thus, such analysis are also a way to verify wether sound event detections by the sensors are accurate.


<div class="row">
  <div class="col-sm-12" style='text-align: center; margin-bottom: 5pt;'>
    <img src="{{ 'noise-pollution-and-perception/images/analysis/birds.png' | relative_url }}" style="max-height: 400pt">
  </div>
</div>

<hr>

Similarly, we can observe the hourly and even quartetly church bells indicating the time of day. Note how the detection varies based on the hour, which matches the varying length of chruch bell sounds as they represent the time of day.

<div class="row">
  <div class="col-sm-12" style='text-align: center; margin-bottom: 5pt;'>
    <img src="{{ 'noise-pollution-and-perception/images/analysis/church.png' | relative_url }}" style="max-height: 400pt">
  </div>
</div>

We are now working on comparing the sound environment of different locations in Delft to find distint and relevant patterns in noise pollution. This work is still ongoing.

## Monitoring construction noise in Amsterdam

The Amsterdam Institute for Advanced Metropolitan Solutions (AMS Institute) in collaboration with the City of Amsterdam and the CityAI Lab deployed 12 of our sensors to monitor construction site noise in Amsterdam. For this purpose, the predictive model has been retrained to detect a variety of construction noises.

<div class="row">
  <div class="col-sm-12" style='text-align: left; margin-bottom: 5pt;'>
    <a href="https://responsiblesensinglab.org/projects/smart-sensors-to-understand-construction-noise">
      <img src="{{ 'noise-pollution-and-perception/images/ams.webp' | relative_url }}" style="max-height: 280pt">
    </a>
  </div>
</div>


More information about this project can be found on the website of the <a href="https://responsiblesensinglab.org/projects/smart-sensors-to-understand-construction-noise">Responsible Sensing Lab</a>.


## Noise annoyance, personality, and health: a longitudinal study
Correlations between noise and cardiovascular diseases have been extensivly studied. The majority of these studies rely on cross-sectional data of noise expose or noise annoyance and health. In this study (work in progress) we define different noise annoyance profiles from longitudinal data and investigate the cummulative effect of noise annoyance on health. Furthermore, we analyse the effect of personality traits on the chance of belonging to a specific noise annoyance profile. Lastly, we attempt to analyse the direction of causality, checking for possible reverse effects from deteriorating health conditions on increased self-reported noise annoyance. For this purpose, a longitudinal latent class analysis was performed and several cross-lagged panel models have been estimated. Preliminary results show that noise annoyance remains relatively constant over time: 75% of participants are generally not annoyed by street noises, 6% are chronically annoyed, and only 19% are occasionally annoyed, thus varying within the 8 years of observation. 3 of the Big Five personality traits were found to significantly affect noise annoyance class memberships: Subjects scoring high on extraversion and emotional stability are less likely to be chronically annoyed, while subjects scoring high on intellect and imagination are more likely to be chronically annoyed. Chronic noise annoyance was found to be correlated with heart complaints and sleeping problems. No significant correlation with heart attacks or high blood pressure was found. The Cross-Lagged Panel Models indicate a possible reverse effect from sleeping problems on self-reported noise annoyance. However, due to limitations of the panel data further research into possible reverse effects is necessary. 

We refer to the published <a href="https://journals.lww.com/nohe/fulltext/2025/01000/longitudinal_analysis_of_the_influence_of.12.aspx">scientific paper</a> for more information about this study.

### Contact
{: #contact}

<div class="card contact-card" style="max-width: 360px;">
  <div class="row g-0">
    <div class="col-4">
      <a href="https://www.tudelft.nl/en/staff/l.cassens/">
        <img src="{{ 'assets/images/team/lion.webp' | relative_url }}" class="contact-avatar">
      </a>
    </div>
    <div class="col-8">
      <div class="card-body">
        <h5 class="card-title"><a href="https://www.tudelft.nl/en/staff/l.cassens/">Lion Cassens</a></h5>
        <p class="card-text">
          PhD Candidate<br>
          <a href="mailto:L.Cassens@tudelft.nl">L.Cassens@tudelft.nl</a><br>
          <a href="https://www.linkedin.com/in/lion-cassens/">
            <img style="color: blue" src="{{ 'assets/images/linkedin.svg' | relative_url }}"  alt="LinkedIn"/>
          </a>
        </p>
      </div>
    </div>
  </div>
</div>