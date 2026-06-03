---
layout: default
title: Understanding, automating, and assisting choice modeller's workflows through AI
---

<ul class="nav project-nav col-12 col-lg-auto me-lg-auto mb-2">
  <li><a href="#contact" class="nav-link px-2">Contact</a></li>
</ul>

## Understanding, automating, and assisting choice modeller's workflows through AI

<div class="row">

  <div class="col-md-8 col-sm-12">  
    <br>
    <p>
    Discrete choice modelling is a widely used approach for understanding and forecasting how people make choices. It is applied in many fields, such as transportation, marketing, energy, and health, to study choices between alternatives (e.g. choosing a transport mode, a product, or a service). These models help researchers and practitioners understand preferences, estimate how much people value certain attributes, and provide insights to support policies.
    </p>
    <p>
    Although discrete choice models are grounded in behavioural theory and statistical methods, developing them  remain deeply influenced by <em>choice modellers' workflows</em>. This process usually involves several iterative stages, including data collection, exploratory analysis, model specification, estimation, interpretation of results, and reporting. These decisions significantly influence the modelling results! 
    </p>
    <p>
      While this flexibility promotes exploration and efficient methodological progress, it also carries the risk of poor decisions, limits reproducibility, and hamper discussion about good practices in the community.
    </p>
    <p>
     My PhD focuses on understanding and supporting discrete choice modellers’ workflows using artificial intelligence. The research started with the development of a Serious Game to study how choice modellers explore data, test models, and make modelling decisions in practice. Building on these insights, the research then progressed toward the design and training of a reinforcement learning–based agent, Delphos, aimed at assisting modellers during the model specification process.
    </p>
  </div>
  <div class="col-md-4 col-sm-12 text-center d-flex align-items-center justify-content-center">
    <img src="{{ 'ai-choice-modelling/DCM_workflow.png' | relative_url }}" alt="DCM Workflow" class="img-fluid" style="max-width: 100%; height: auto; padding-bottom: 20px;">
  </div>

  <div class="col-sm-12">
    <br>
    <h3>(4) Delphos: A Multitask Reinforcement Learning Agent</h3>
    <p>
    We are extending Delphos, our reinforcement learning agent to work with multiple discrete choice datasets at once. This will allow the agent to learn from a broader range of datasets and to be applied to new datasets without the need for retraining. Specifically, Delphos treats the model specification process as a sequential decision-making process, where the agent iteratively modifies model specifications and receives feedback from the estimation environment based on model fit and convergence. We are currently training the agent on several discrete choice datasets to allow the agent to learn transferable modelling strategies that can generalise beyond a single dataset or application.
    </p>

    <div class="alert alert-warning" role="alert">
      <strong><a href="{{ 'ai-choice-modelling/Delphos_v2.pdf' | relative_url }}" target="_blank" class="alert-link">Working Paper:</a></strong> This work will be presented at the <em>International Choice Modelling Conference 2026</em>, Australia.
    </div>

    <p>
    We are actively collecting transport choice datasets suitable for further training our agent.
    </p>

    <div class="alert alert-info" role="alert">
      <details>
        <summary><strong>View Current Transport Choice Datasets (Examples)</strong></summary>
        <ul class="mt-2 mb-0">
          <li>Netherlands Mode Choice (<code>1987_netherlands_modechoice</code>)</li>
          <li>UK Value of Time (<code>1994_uk_vot</code>)</li>
          <li>Swissmetro (<code>2001_swissmetro</code>)</li>
          <li>Norway VTT (<code>2009_norway_vtt</code>)</li>
          <li>Arentze 2013 (<code>2013_Arentze</code>)</li>
          <li>Spain Parking Choice (<code>2014_spain_parkingchoice</code>)</li>
          <li>Netherlands Flight Choice (<code>2016_netherlands_flightchoice</code>)</li>
          <li>Apollo Route Choice (<code>2018_apollo_routechoice</code>)</li>
          <li>London Mode Choice (<code>2018_london_modechoice</code>)</li>
          <li>OPTIMA Mode Choice (<code>2018_optima_modechoice</code>)</li>
        </ul>
      </details>
    </div>
    <br>
    <h3>(3) Delphos: Reinforcement Learning for Choice Model Specification</h3>
    <p>
    Our latest project introduces <strong>Delphos <a href="https://arxiv.org/pdf/2506.06410" target="_blank">(paper)</a></strong>, a reinforcement learning framework designed to assist analysts in the complex task of specifying discrete choice models. Selecting an appropriate model is often iterative and time-consuming due to the many modelling decisions involved, particularly when exploring nonlinear transformations, capturing observed heterogeneity, and meeting nehavioural expectations.
    </p>
    <p>
    This project formalises an agent-environment interaction to automate the model specification process. This interaction is modelled as a Markov Decision Process, in which a Deep Q-Network agent sequentially takes actions to constructs model specifications. The environment estimates these models, evaluates their performance, and provides feedback using model fit or behavioural expectations, as depicted in the below Figure:
    </p>
    <p>
    This work demonstrates how RL can support analysts by exploring broad specification spaces, proposing well-performing models, and reducing repetitive manual effort.
    </p>
    <div class="alert alert-warning" role="alert">
      <strong><a href="{{ 'ai-choice-modelling/Delphos_v1.pdf' | relative_url }}" target="_blank" class="alert-link">Paper under review</a></strong>
    </div>
    <!--
    <div style="text-align:center;">
    <iframe width="560" height="315"
            src="https://www.youtube.com/embed/4m3Pjy-sEEQ"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
    </iframe>
    </div>
    -->
    <div class="col-sm-12" style="text-align: center;">
    <iframe src="{{ 'ai-choice-modelling/hEART_2025.pdf' | relative_url }}" width="80%" height="500px" style="border: none;"></iframe>
    <p>
      <a href="{{ 'ai-choice-modelling/hEART_2025.pdf' | relative_url }}" target="_blank">📥 Download</a>
    </p>
    </div>
    <br><br>
    <h3>(2) Large Language Models as Modelling Assistants</h3>
    <p>
    This project investigates how <strong>Large Language Models (LLMs)</strong> can assist or collaborate with analysts when formulating discrete choice models. Since LLMs are increasingly capable of generating domain-relevant knowledge, we not only explore the ability of LLMs to propose model specifications, but also to code and estimate them.
    </p>
    <p>
    This work then examines various prompting strategies, model consistency, and the strengths and limitations of current LLMs for suporting choice modelling workflows. This research positions LLM-based assistants as emerging tools that can accelerate exploratory analysis, support model refinement, and complement human expertise in behavioural modelling
    </p>
    <div class="alert alert-warning" role="alert">
      <strong><a href="{{ 'ai-choice-modelling/LLM_DCM.pdf' | relative_url }}" target="_blank" class="alert-link">Paper under review</a></strong>
    </div>
    <div class="col-sm-12" style="text-align: center;">
      <iframe src="{{ 'ai-choice-modelling/LLM_MNL_Results.pdf' | relative_url }}" width="80%" height="500px" style="border: none;"></iframe>
      <p>
        <a href="{{ 'ai-choice-modelling/LLM_MNL_Results.pdf' | relative_url }}" target="_blank">📥 Download</a>
      </p>
    </div>
    <br><br>
    <h3>(1) Understanding Modellers: The Serious Choice Modelling Game</h3>
    <p>
    Our foundational project introduces the <strong><a href="http://dcm-serious-game.tudelft.nl/?Session_id=test">Serious Choice Modelling Game</a></strong>, which mimics the actual modelling process. This allows us to capture and analyse the decision-making processes of modellers during the descriptive data analysis, model specification, outcome interpretation, and reporting phases. Participants were asked to develop choice models using a stated preference dataset to inform policymakers about individual willingness-to-pay values.
    </p>
    <p>
    This setup allows us to observe how modellers behave in practice—how they explore data, specify choice models, and interpret outcomes. The results reveal substantial variation in descriptive approaches, modelling strategies, and willingness-to-pay values. These findings provide an empirical basis for understanding modelling behaviour and highlight the need for tools that support transparency, reproducibility, and methodological learning.
    </p>
    <p>
    To facilitate future research, the source code and installation instructions for the Serious Choice Modelling Game are publicly available on GitHub. The repository can be accessed at <a href="https://github.com/TUD-CityAI-Lab/DCM-SG" target="_blank">https://github.com/TUD-CityAI-Lab/DCM-SG</a>.
    </p>
    <div class="col-sm-12" style="text-align: center;">
      <img src="{{ 'ai-choice-modelling/DCM_overview.png' | relative_url }}" alt="Conceptual overview of the choice modelling research process (Nova et al., 2024)" style="max-width: 50%; height: auto;">
      <p><em>Conceptual overview of the choice modelling research process</em></p>
    </div>
    <div class="col-sm-12" style="text-align: center;">
      <iframe src="{{ 'ai-choice-modelling/IATBR_2024_ok.pdf' | relative_url }}" width="80%" height="500px" style="border: none;"></iframe>
      <p>
        <a href="{{ 'ai-choice-modelling/IATBR_2024_ok.pdf' | relative_url }}" target="_blank">📥 Download</a>
      </p>
    </div>
    <br>
    <br>
    <h3>MSc theses</h3>
    <ul>
      <li>
        <strong>Exploring the Enhancement of Predictive Accuracy for Minority Classes in Travel Mode Choice Models</strong><br>
        <em>Author:</em> Aspasia Panagiotidou (TU Delft)
      </li>
      <li>
        <strong>Analysis of the Contribution of Explanatory Factors on the Predicted Choice Probabilities Derived from the L-MNL Using the SHAP Method: A Mode Choice Application</strong><br>
        <em>Author:</em> Exequiel Salazar (Universidad de Concepción)
      </li>
    </ul>

<div class="col-sm-12">
  <br>  
  <h3>Current MSc Projects</h3>
  <p>
    We welcome motivated MSc students interested in contributing to innovative research at the intersection of behavioural modelling, machine learning, and human–AI collaboration. Below are some examples of ongoing or proposed topics:
  </p>

  <ul>
    <li>
      <strong>Reinforcement learning for discrete choice modelling</strong><br>
      <p>
        Develop and evaluate RL agents that explore specification spaces, incorporate expert knowledge or behavioural constraints, and extend Delphos to models with unobserved heterogeneity (e.g., latent classes, mixed logit). Opportunities also exist for creating new RL environments or improving the agent’s state representations.
      </p>
    </li>

    <li>
      <strong>Immersion in gaming environments</strong><br>
      <p>
        Analyse physiological signals collected while participants play a horror video game on traditional monitors or in virtual reality. Potential topics include identification of visual and audio factors that trigger responses, sequential modelling of physiological reactions, or designing predictive stress-response models.
      </p>
    </li>

  </ul>
</div>
<br>
<br>
<div class="card contact-card" style="max-width: 360px;">
  <div class="row g-0">
    <div class="col-4">
        <a href="https://www.tudelft.nl/en/staff/g.nova/?">
          <img src="{{ 'assets/images/team/gabriel.webp' | relative_url }}" class="contact-avatar" >
        </a>
    </div>
    <div class="col-8">
      <div class="card-body">
        <h5 class="card-title"><a href="https://www.tudelft.nl/en/staff/g.nova/?">Gabriel Nova</a></h5>
        <p class="card-text">
          PhD Candidate<br>
          <a href="mailto:G.Nova@tudelft.nl">G.Nova@tudelft.nl</a><br>
          <a href="https://www.linkedin.com/in/gabriel-nova-sep%C3%BAlveda-870855100/">
            <img style="color: blue" src="{{ 'assets/images/linkedin.svg' | relative_url }}" alt="LinkedIn"/>
          </a>
        </p>
      </div>
    </div>
  </div>
</div>
</div>
</div>
