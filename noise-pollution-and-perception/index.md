---
layout: default
title: "Listening to our Cities: Using Smart Sensors and Machine Learning to Study Urban Noise Pollution"
---

<ul class="nav project-nav col-12 col-lg-auto me-lg-auto mb-2">
  <li><a href="#contact" class="nav-link px-2">Contact</a></li>
</ul>

## Listening to our Cities: Using Smart Sensors and Machine Learning to Study Urban Noise Pollution

The sound of urban environments is often dominated by noise from transportation and residents, with profound effects on health and wellbeing. Higher noise exposure has been correlated with higher stress levels, sleep disruptions and cardiovascular diseases. In order to understand and mitigate noise pollution in the urban environment, sophisticated information on the local soundscape is neccessary. Current noise mapping efforts are often based on averaged sound levels for day, evening, and night time. While such aggregations are widely available and simplify noise mapping, they do not capture many aspects of the human perception of noise. For example, a constant background noise may have different effects than high-peak noise events, yet both could result in the same averaged sound level. Furthermore, such measures only account for the perceived loudness, but ignore other knowledge on the perception of sound, such as roughness, or perceived annoyance.

The goal of this project is to develop techniques for holistic noise maps, which takes into account how we as humans perceive urban noise. For this purpose, we are developing smart sensors, which utilize edge processing and machine learning to predict the source of noise events, and its perception based on various noise metrics. The audio signal is directly processed on the device, to ensure the privacy of the public. Furthermore, the sensor is self-sufficient and powered by battery and solar power, making it easy to use for real-world research. We plan to deploy a large array of such sensors to understand how our cities shape the sounds around us. In a later step, the recorded noise metrics will be used to develop a predictive model, allowing to estimate the urban soundscape of other cities based on ubiquitous data on the road networks, built environment and neighbourhood characteristics. 

![Noise mapping with smart sensors]({{ 'noise-pollution-and-perception/images/sensor_noise_mapping.jpg' | relative_url }})

### Urban soundscape sensor
The soundscape sensor is currently under development and will be open sourced after completion ([follow on GitHub](https://github.com/cityai-soundscapes)).

The images below shows the current prototype. The deployment of 40 sensors is planned for Summer 2024 in Amsterdam.

<div class="row">
  <div class="col-sm-6" style='text-align: center'>
    <img src="{{ 'noise-pollution-and-perception/images/sensor_deployed.webp' | relative_url }}" style="max-height: 330pt">
  </div>
  <div class="col-sm-6" style='text-align: center'>
    <img src="{{ 'noise-pollution-and-perception/images/sensor_board.webp' | relative_url }}" style="max-height: 330pt">
  </div>
</div>

<br>


## Noise annoyance, personality, and health: a longitudinal study
Correlations between noise and cardiovascular diseases have been extensivly studied. The majority of these studies rely on cross-sectional data of noise expose or noise annoyance and health. In this study (work in progress) we define different noise annoyance profiles from longitudinal data and investigate the cummulative effect of noise annoyance on health. Furthermore, we analyse the effect of personality traits on the chance of belonging to a specific noise annoyance profile. Lastly, we attempt to analyse the direction of causality, checking for possible reverse effects from deteriorating health conditions on increased self-reported noise annoyance. For this purpose, a longitudinal latent class analysis was performed and several cross-lagged panel models have been estimated. Preliminary results show that noise annoyance remains relatively constant over time: 75% of participants are generally not annoyed by street noises, 6% are chronically annoyed, and only 19% are occasionally annoyed, thus varying within the 8 years of observation. 3 of the Big Five personality traits were found to significantly affect noise annoyance class memberships: Subjects scoring high on extraversion and emotional stability are less likely to be chronically annoyed, while subjects scoring high on intellect and imagination are more likely to be chronically annoyed. Chronic noise annoyance was found to be correlated with heart complaints and sleeping problems. No significant correlation with heart attacks or high blood pressure was found. The Cross-Lagged Panel Models indicate a possible reverse effect from sleeping problems on self-reported noise annoyance. However, due to limitations of the panel data further research into possible reverse effects is necessary. The results of this study will be presented at the International Congress of Sound and Vibration ([ICSV](https://www.icsv30.org/)) 30 in Amsterdam.

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