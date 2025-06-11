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
    While the literature on Choice modelling offers extensive knowledge about diverse modelling approaches, it falls short in fully capturing the decision-making process that modellers undertake across research phases. These decisions significantly influence the modelling results, especially as modellers have degrees of freedom in choosing, adjusting, and interpreting model specifications based on analyses carried out in previous phases. Although this flexibility promotes exploration and efficient methodological progress, it also carries the risk of poor decisions, limits reproducibility, and hamper discussion about good practices in the community.
    </p>
    <br>
    <h3>Projects</h3>
    <p>
    To address these research gaps, our first project introduces the <strong><a href="http://dcm-serious-game.tudelft.nl/?Session_id=test">Serious Choice Modelling Game</a></strong>, which mimics the actual modelling process. This allows us to capture and analyse the decision-making processes of modellers during the descriptive data analysis, model specification, outcome interpretation, and reporting phases. Participants were asked to develop choice models using a stated preference dataset to inform policymakers about individual willingness-to-pay values. Their workflows reveal variability among the descriptive analysis approaches used, the way they navigate across model specifications, and the reported willingness-to-pay.
    </p>    
  </div>

  <div class="col-sm-12" style="text-align: center;">
    <img src="{{ 'ai-choice-modelling/DCM_overview.png' | relative_url }}" alt="Conceptual overview of the choice modelling research process (Nova et al., 2024)" style="max-width: 50%; height: auto;">
    <p><em>Conceptual overview of the choice modelling research process</em></p>
  </div>
  <div class="col-sm-12" style="text-align: center;">
    <iframe src="{{ 'ai-choice-modelling/IATBR_2024_ok.pdf' | relative_url }}" width="80%" height="500px" style="border: none;"></iframe>
    <p>
      <a href="{{ 'ai-choice-modelling/IATBR_2024_ok.pdf' | relative_url }}" target="_blank">📥 Download PDF</a>
    </p>
  </div>
  <br>
  <br>
  <div class="col-sm-12">
    <br>
    <p>
    Our second project aims to develop tools to support choice modellers in their process of finding model specifications that capture decision-makers' choice process. Extracting meaningful insights from such models then requires the careful selection of an appropriate specification, an iterative process that is often time-consuming due to the many modelling decisions involved. 
    </p>
    <p>
    This project introduces a reinforcement learning framework, which formalises an agent-environment interaction to automate the model specification process in discrete choice models. This interaction is modelled as a Markov Decision Process, in which a Deep Q-Network agent sequentially takes actions to propose a model specification, while an environment performs the estimation process and returns feedback based on the modelling outcomes, as depicted in the below Figure:
    </p>
    </div>
    <div class="col-sm-12" style="text-align: center;">
      <img src="{{ 'ai-choice-modelling/dcm_rl.png' | relative_url }}" alt="DQN agent - DCM environment framework" style="max-width: 50%; height: auto;">
      <p><em>Delphos: A DQN agent that automate the utility specification process</em></p>
    </div>
    <div class="col-sm-12" style="text-align: center;">
    <iframe src="{{ 'ai-choice-modelling/hEART_2025.pdf' | relative_url }}" width="80%" height="500px" style="border: none;"></iframe>
    <p>
      <a href="{{ 'ai-choice-modelling/hEART_2025.pdf' | relative_url }}" target="_blank">📥 Download PDF</a>
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
  </div>

  <div class="col-sm-12">
  <br>
  <h3>MSc projects</h3>
  <p>
    Are you interested further expanding choice modeling with cutting-edge AI techniques? We welcome students looking to conduct their thesis on projects that address innovative problem in this field.
  </p>
  <ul>
    <li>
      <strong>Reinforcement learning for discrete choice modeling</strong><br>
      <p>
        (1) Develop robust RL agents to support analysts in exploring the model specifications space. (2) Collaborate in the design of RL environments that incorporate human knowledge, can reflect behavioral constraints, and extend to other model families such as unobserved heterogeneity and latent class models.
      </p>
    </li>
    <li>
      <strong>Immersion in Gaming Environments</strong><br>
      <p>
        Data collected: Physiological responses were measured while participants played a scary video game on different platforms, such as traditional monitors and virtual reality. You could move forward in understanding the visual and/or audio factors of terror that lead to physiological changes or responses. 
      </p>
    </li>   
  </ul>
</div>

<br>

### Contact{: #contact}

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