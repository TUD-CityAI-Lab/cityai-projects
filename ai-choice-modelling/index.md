---
layout: default
title: Understanding, automating, and assisting choice modeller's workflows through AI
---

<ul class="nav project-nav col-12 col-lg-auto me-lg-auto mb-2">
  <li><a href="#contact" class="nav-link px-2">Contact</a></li>
</ul>

## Understanding, automating, and assisting choice modeller's workflows through AI

<div class="row">

  <div class="col-sm-12">  
    <p>
    Discrete choice modelling is a robust modelling framework for understanding and forecasting human choice behaviour across various fields. These models are typically used to infer individual preferences, estimate consumers’ willingness to pay, generate behavioural insights that inform policy decisions. Unlike traditional approach, this research is considered as an art form. This perspective arise from the need to blend formal behavioural theories, statistical methodologies, and the judgments of choice modellers up to reporting results in the iterative journey from data collection trough descriptive analysis, models specification, outcome interpretation to the reporting of the results.
    </p>
    <p>
    Yet, despite their formal structure, choice models remain deeply influenced by </em>choice modellers' workflows</em>. Modellers make a wide range of analytical decisions—data collection, data exploration, model specification, model estimation, interpretation, and reporting. These decisions significantly influence the modelling results! Although this flexibility promotes exploration and efficient methodological progress, it also carries the risk of poor decisions, limits reproducibility, and hamper discussion about good practices in the community.
    </p>
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
    <div style="text-align:center;">
    <iframe width="560" height="315" 
            src="https://www.youtube.com/embed/4m3Pjy-sEEQ" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
    </iframe>
  </div>
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
    <p>
    This work then examines various prompting strategies, model consistency, and the strengths and limitations of current LLMs for suporting choice modelling workflows. This research positions LLM-based assistants as emerging tools that can accelerate exploratory analysis, support model refinement, and complement human expertise in behavioural modelling
    </p>  
    <p>
    You can find our latest work at:<br>
    <a href="https://arxiv.org/pdf/2507.21790" target="_blank">https://arxiv.org/pdf/2507.21790</a>
    </p>  
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