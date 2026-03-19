---
layout: default
title: "Listening to our Cities: Using Smart Sensors and Machine Learning to Study Urban Noise Pollution"
---

<ul class="nav project-nav col-12 col-lg-auto me-lg-auto mb-2">
  <li><a href="#overview" class="nav-link px-2">Overview</a></li>
  <li><a href="#sensor" class="nav-link px-2">Sensor</a></li>
  <li><a href="#sed-trade-off" class="nav-link px-2">Sound Event Detection</a></li>
  <li><a href="#noise-monitoring-delft" class="nav-link px-2">Delft Case Study</a></li>
  <li><a href="#Construction-noise-amsterdam" class="nav-link px-2">Construction Noise</a></li>
  <li><a href="#noise-personality-health" class="nav-link px-2">Personality & Health</a></li>
  <li><a href="#contact" class="nav-link px-2">Contact</a></li>
</ul>

## Listening to our Cities: Using Smart Sensors and Machine Learning to Study Urban Noise Pollution
{: #overview}


The sound of urban environments is often dominated by noise from transportation and human activity, with profound effects on health and well-being. Higher noise exposure has been linked to increased stress levels, sleep disturbances, and cardiovascular diseases. To better understand and mitigate noise pollution in cities, more detailed information on the local soundscape is required. Current noise mapping efforts are typically based on averaged sound levels for day, evening, and night. While such aggregations are widely available and simplify large-scale assessments, they fail to capture many aspects of how noise is perceived. For example, constant background noise may have very different effects than short, high-peak events, even when resulting in the same average level. Moreover, these measures focus primarily on loudness and overlook other perceptual characteristics of sound.

In this PhD project, we combine machine learning, sensing, and perception research to gain a more complete understanding of urban noise; how it can be measured and how it affects people. Our work includes the development of low-cost, privacy-friendly sensors and their deployment in real urban environments. We further apply statistical methods to better understand how noise relates to human perception, behaviour, and health. 

You can find an overview of the projects below. If you are interested in a scientific collaboration, feel free to get in touch via the <a href="#contact">contact details</a> provided at the end of the page.

---

## 1. Low-cost solar-powered urban soundscape sensor
{: #sensor}

<div class="row g-4 align-items-start mb-2">
  <div class="col-12 col-lg-7">
    <p>To study urban soundscapes at scale, we developed a low-cost sensor to measure sound levels and detect sound events. The sensor is powered by a solar panel and battery for easy deployment without the need for mains power. The sensor is privacy friendly and processes audio directly on the device, can transmit aggregated indicators via LoRaWAN while storing more detailed metrics on a micro SD card.</p>

    <p>Unlike conventional sound level meters, the sensor does not only measure how loud the environment is. It also estimates which sound sources are present, such as traffic, birds, speech, sirens, or aircraft, and derives complementary acoustic indicators such as intermittency and sharpness. Because all processing happens on the sensor itself, no raw audio needs to be recorded or transmitted.</p>

    <figure class="mb-0">
      <img src="{{ 'noise-pollution-and-perception/images/sensor-diagram.png' | relative_url }}" alt="Urban soundscape sensor overview diagram" class="img-fluid">
    </figure>

    <p>The hardware and firmware are open source and have been <a href="https://doi.org/10.1016/j.ohx.2026.e00753">published in HardwareX</a>.</p>

  </div>
  <div class="col-12 col-lg-5">
    <figure class="mb-0">
      <img src="{{ 'noise-pollution-and-perception/images/soundscape-sensor-terrace.webp' | relative_url }}" alt="Solar-powered soundscape sensor on a terrace" class="img-fluid">
      <figcaption class="figure-caption mt-2">Solar-powered soundscape sensor installed on a terrace.</figcaption>
    </figure>
  </div>
</div>
---

## 2. Sound event detection on the edge: Exploring the trade-off between accuracy and efficiency
{: #sed-trade-off}

<div class="row g-4 align-items-start mb-2">
  <div class="col-12 col-lg-7">
    <p>Sound source classification adds important context to noise monitoring. To preserve privacy, it is often paramount to run such predictive models directly on a sensor, which introduces strict limits in memory, computation, and energy use. Especially when sound event detection should run on solar-powered devices.</p>

    <p>In this project, we train sound event detection models that can run on constrained hardware. To improve real-world performance, we collected a dataset of urban sounds in the Netherlands, allowing us to train models tailored to the Dutch urban soundscape rather than relying only on generic datasets.</p>

    <p>We systematically study the trade-off between model accuracy and efficiency under microcontroller constraints for real-time classification. Our results show that larger models do not necessarily perform better in practice: while they can achieve slightly higher accuracy, they often fail to meet real-time or energy requirements. Thus, we identify a small set of <strong>Pareto-optimal models</strong> that balance accuracy and efficiency. These models require ten to a few hundred kilobytes of memory and run in real time on an ESP32-S3 microcontroller.</p>

    <p>The developed model is the basis for the sound event detection on our soundscape sensor.</p>

    <p><a href="https://pure.tudelft.nl/ws/portalfiles/portal/264371059/000940.pdf">Read the conference paper</a></p>
  </div>
  <div class="col-12 col-lg-5">
    <figure class="mb-0">
      <img src="{{ 'noise-pollution-and-perception/images/mel-spectrograms-edge-sed.png' | relative_url }}" alt="Mel spectrograms used for edge sound event detection" class="img-fluid">
      <figcaption class="figure-caption mt-2">Figure: Mel-spectrograms of three different sizes for edge sound event detection</figcaption>
    </figure>
  </div>
</div>

---

## 3. Citizen science soundscape monitoring in Delft
{: #noise-monitoring-delft}

<div class="row g-4 align-items-start mb-2">
  <div class="col-12 col-lg-7">
    <p>In Summer 2025, we deployed 39 ofour solar-powered sensors in Delft with the help of residents willing to install such a sensor at their home.  The deployment combined source-aware sound measurements with survey data on perceived presence of sounds and noise annoyance.</p>

    <p>The results show that urban sound environments are very heterogeneous. Different locations may have similar average loudness levels while still differing strongly in intermittency, dominant sound sources, and perceived annoyance. Sound event-aware sensors thus offer valuable complementary information to traditional sound pressure levels.</p>

    <p>The Delft study also shows the value of distinguishing between overall source presence and sources causing disruptive, short sound peaks. For example, louder and intermittent traffic noise from a loud vehicle may cause more annoyance than mere background noise from distant traffic.</p>
    
    <p>We found that human chatter and church bell ringing is unique to Delft's historic old town. More detailed maps and temporal analyses are available in the <a href="https://dx.doi.org/10.2139/ssrn.6428959">preprint</a>.</p>

    

    <p><a href="https://dx.doi.org/10.2139/ssrn.6428959">Read more in the article preprint</a></p>

    <figure class="mt-3 mb-0">
      <img src="{{ 'noise-pollution-and-perception/images/analysis/birds.png' | relative_url }}" alt="Bird sound analysis in Delft" class="img-fluid">
    </figure>
  </div>
  <div class="col-12 col-lg-5">
    <figure class="mb-0">
      <img src="{{ 'noise-pollution-and-perception/images/deploying-sensor.webp' | relative_url }}" alt="Deploying a sensor in Delft" class="img-fluid">
    </figure>
    <figure class="mt-3 mb-0">
      <img src="{{ 'noise-pollution-and-perception/images/analysis/church-bell-sounds-delft.png' | relative_url }}" alt="Church bell sounds in Delft" class="img-fluid">
    </figure>
  </div>
</div>

---

## 4. Monitoring construction site noise in Amsterdam
{: #Construction-noise-amsterdam}

<div class="row g-4 align-items-start mb-2">
  <div class="col-12 col-lg-7">
    <p>Our sensor platform has also been used to monitor construction site noise in Amsterdam. The Amsterdam Institute for Advanced Metropolitan Solutions (AMS Institute) in collaboration with the City of Amsterdam and the CityAI Lab deployed 12 sensors at three construction sites. For this purpose, the AMS retrained the sound event detection model for a variety of construction noises.</p>

    <p>More information can be found at the <a href="https://responsiblesensinglab.org/projects/smart-sensors-to-understand-construction-noise">Responsible Sensing Lab, AMS Institute</a>.</p>
  </div>
  <div class="col-12 col-lg-5">
    <figure class="mb-0">
      <img src="{{ 'noise-pollution-and-perception/images/ams.webp' | relative_url }}" alt="Solar-powered sound sensor mounted in Amsterdam" class="img-fluid">
      <figcaption class="figure-caption mt-2">Solar-powered sound sensor mounted in Amsterdam</figcaption>
    </figure>
  </div>
</div>

---

## 5. Interactions among long-term noise exposure, personality and health
{: #noise-personality-health}

Beyond measuring the sound environment itself, we also study how noise is experienced by people over time. Most existing research on noise annoyance and health is based on cross-sectional data, which makes it difficult to examine longer-term patterns and the direction of effects.

In this project, we analyse eight years of longitudinal panel data from the Netherlands to better understand how noise annoyance develops, how stable it is, and how it relates to personality and health outcomes. The results indicate that annoyance is relatively stable over time for most participants, depending on the noise source considered. At the same time, clear differences exist between groups of people who are rarely annoyed, occasionally annoyed, or chronically annoyed.

We also find that personality matters. Extraversion and emotional stability are associated with a lower likelihood of chronic annoyance, while intellect or imagination is associated with a higher likelihood. In addition, the results suggest that the relationship between annoyance and health may not be one-directional: negative health outcomes may also increase the sensitivity to noise and thus, noise annoyance.

[Read the paper](https://doi.org/10.4103/nah.nah_107_24)

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