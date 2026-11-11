# Background

## Genomics in clinical and public health practice

Genomics is now embedded across the clinical and public health landscape, with sequencing technologies increasingly used to support diagnostics (e.g. identifying pathogenic variants in rare disease or hereditary cancer), guide personalised treatment decisions (e.g. selecting targeted therapies based on tumour mutation profiles or choosing effective antiretroviral regimens informed by HIV drug‑resistance mutations), early detection of disease (e.g. use of circulating tumour DNA for early cancer detection), and inform public health surveillance (e.g. tracking antimicrobial resistance and monitoring pathogen outbreaks). In each of these diverse applications, bioinformatics pipelines sit between the raw sequencing data and the result a clinical or public health team acts on.

---

## Pipelines are multi-component and often complex

A bioinformatics pipeline is not a single piece of software but a chain of processes, each depending on the one before it. In human genetics, this chain typically includes read filtering, alignment, variant calling, variant annotation, and variant prioritisation. In pathogen genomics, the chain is usually different, often including host read removal, taxonomic classification, *de novo* assembly, assembly polishing, and detection of antimicrobial or antiretroviral resistance genes.

Regardless of the specific steps a given pipeline includes, all pipelines share the same underlying property: each component introduces its own assumptions, dependencies, and potential points of failure, and these accumulate to determine the accuracy and reliability of the final result. Pipeline performance is also sensitive to software versions, algorithmic choices, parameter settings, reference datasets, and the computational environment in which they are deployed. Taken together, these factors create multiple compounding sources of variability that can affect the consistency, reproducibility, and clinical robustness of genomic analyses.

---

## ISO 15189 and why accreditation matters

Bioinformatics pipelines used in clinical or public health settings fall within scope of ISO 15189, the well-established and internationally recognised quality and regulatory framework which defines the requirements for competence, method validation, and quality management in medical laboratories. Although the standard was written primarily with wet laboratory processes in mind, its requirements apply equally to the computational analyses that contribute to a clinical result.

Accreditation against ISO 15189 provides an independent, standardised assessment of a laboratory's technical competence and by extension the reliability of the results it produces. For genomic services, accreditation offers assurance that bioinformatics pipelines have been validated appropriately, are operating within controlled quality management systems, and consistently meet predefined performance criteria. This strengthens confidence among clinicians and patients, and it facilitates interoperability and trust between laboratories, enabling the exchange of genomic data where governance permits and supporting multi-centre clinical pathways. In a field where analytical methods evolve rapidly, accreditation is what keeps laboratory processes transparent, reproducible, and demonstrably fit for clinical use as those methods change.

Central to accreditation is the principle of validation, in which a laboratory must demonstrate that its examination methods are fit for their intended purpose against **predefined performance criteria**. Section 2 sets out what validation means under ISO 15189 in full. Here we focus on why validating the bioinformatics component of that process is particularly difficult.

---

## What makes bioinformatics validation difficult

Bioinformatics is one component of a wider end-to-end examination process, but it does not validate in the same way as a wet laboratory method. A pipeline is a chain of interacting components rather than a single assay, so a validation study has to account for interactions between those components, not just their individual performance. Software and reference datasets are updated far more frequently than wet laboratory reagents or platforms, and each update can shift pipeline output in ways that are hard to predict in advance. The range of sequencing platforms and sample types encountered in clinical practice adds further variability that a validation study needs to capture.

This is compounded by the reference materials available. Well characterised reference materials exist for many wet laboratory assays, but for a large number of clinically relevant variants, pathogens, or genomic features, equivalent bioinformatics reference materials are limited or absent, forcing laboratories to rely on incomplete truth sets instead. Differences in computational infrastructure and workflow management systems between laboratories add a further layer of complexity that has no real wet laboratory equivalent. Together, these factors make it difficult to design a bioinformatics validation study that is comprehensive, reproducible, and aligned with what regulators expect.

---

## Variable practice and the case for a consistent approach

No consensus framework currently exists for assessing bioinformatics pipeline performance, so the level of evidence supporting pipeline accuracy and robustness differs substantially from one institution to the next. A shared standard would close this gap. It would improve consistency between laboratories, make cooperation and data sharing easier, and provide transparent, comparable evidence of performance. It would also support alignment with ISO 15189 and reduce variation in clinical results that arises simply from differences in pipeline design or implementation.

This guide sets out to provide that standard, presenting validation guidance grounded in the principles and requirements of ISO 15189.
