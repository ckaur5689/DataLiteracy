## Counts vs Rates

 Counts are an important metric to gain a feel for volumes of activity or patients. However they are not useful when comparing with other geographical areas.

 Rates (often per 10,000 or 100,000) are often referred to as "Crude Rates" and offer a fairer way for comparison.

![Alt text](https://github.com/ckaur5689/DataLiteracy/blob/main/images/CountsvsRates.png)


  ## Consideration #1

   What about the scenario when age profiles are different amongst geographical areas?
    
   For example there is are proportionally more working age people in ICB B compared to ICB A or when more people aged 65 and over
   in ICB B compared to ICB A. 
    
![Alt text](https://github.com/ckaur5689/DataLiteracy/blob/main/images/CountsvsRates_AgeProfiles.png)


  This is when it might be appropriate to switch to age standardised rates? For what purpose is it important to switch to these?

  It depends on the purpose of the comparison and what question you are trying to answer.

  For healthcare analytics, the distinction is important because age-standardisation is fundamentally about removing differences in population structure
  so comparisons are fair.
    
      Use national standard populations (e.g. European Standard Population / ESP2013 or directly standardised national populations) when:
        comparing areas fairly
        benchmarking organisations
        tracking inequalities
        publishing comparable rates
        supporting epidemiological/public health interpretation
      
      Use actual local population cohorts or age-specific rates when:
        operational planning matters more than comparability
        you want to understand real demand
        analysing service utilisation by age
        working with specific cohorts (e.g. frailty, paediatrics, working-age adults)

 For many NHS operational use cases, age-specific rates are often more interpretable than a single age-standardised figure.

     Crude rates are useful for operational decision making 

 ![Alt text](https://github.com/ckaur5689/DataLiteracy/blob/main/images/CountsvsRates_Age_FullPicture.png)


##Example

Imagine:

    ICB A - younger urban population
    ICB B - older rural/coastal population

ED attendance crude rates may naturally be higher in ICB B because:

      older adults attend ED more often
      more frailty
      more multimorbidity

Age-standardisation removes this structural difference.

That’s useful if asking:

    “Is the underlying utilisation risk genuinely higher?”

But less useful if asking:

    “Which system actually needs more ED capacity?”

Because the actual older population still exists operationally.

For Specific Age Cohorts

If you are already analysing:

    65+
    0–19
    working-age adults
    frailty cohorts

…then applying age-standardisation again can become less meaningful.

Why?

Because you’ve already partially controlled for age through cohort restriction.

In these cases, it’s often better to use:

Age-specific rates

Example:

Cohort	ED Attendances per 100k
0–19	  5,800
20–64	  1,200
65+	    8,700

This is usually:

    easier to interpret
    operationally meaningful
    clinically intuitive
    Practical NHS Guidance

Use ESP / standard populations when:

Public health style comparison
  mortality
  prevalence
  admissions
  inequalities

Benchmarking
  comparing ICBs
  comparing local authorities
  comparing Trust populations

Research / publication
  reproducibility
  comparability

## Use Actual Population Cohorts When:
Operational analytics
    capacity planning
    demand modelling
    workforce planning
    frailty services
    community services

Population health management
  identifying actual burden
  targeting interventions

Service utilisation analysis
  who is using services
  where pressure originates
  
## Very Important Caveat

Age-standardised rates can sometimes obscure true operational burden.

An area with:

  genuinely older populations
  higher frailty
  more multimorbidity

…may appear “average” after standardisation despite facing substantially greater service pressure.

## That’s why executives should usually see BOTH:

    crude rates
    age-standardised rates
    actual counts
    age-specific breakdowns

## Together

A Strong Rule of Thumb

##For fair comparison:

Use age-standardised rates.

##For operational decision-making:

Use actual age-specific demand profiles.

