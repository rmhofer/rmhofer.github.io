<div class="section" id="research">
    <h3 class="scrollable-content-header">Research</h3>

    {% assign a_evolution = site.data.areas | where: "key", "evolution" | first %}
    <div class="research-section" style="border-left-color: {{ a_evolution.color }};">
        <h4>The emergence of combinatorial structure in cultural symbol systems</h4>

        <p>The ability to learn and culturally transmit symbol systems is central to human intelligence. From phonemes in spoken words, to notes in a melody or the lines of a diagram, these systems rely on combinatorial structure (a finite set of building blocks that can be rearranged to compose new concepts). Some of the aspects enabling combinatorial behavior are shared with other animal species but humans put these abilities to unique uses, going far beyond the kinds of systems we see in non-human animals.
        </p>

        <p>How do combinatorial symbol systems emerge? To answer this question, I am developing computational models that enable us to characterize combinatorial structure, assess whether these systems are structured efficiently, and understand their evolutionary dynamics.
        </p>
    </div>

    {% assign a_modeling = site.data.areas | where: "key", "modeling" | first %}
    <div class="research-section" style="border-left-color: {{ a_modeling.color }};">
        <h4>Computational and Bayesian models of cognition</h4>

        <p>A methodological thread running through much of my work is the development of computational models&mdash;often Bayesian, and increasingly neuro-symbolic&mdash;that formalize how people learn, represent, and reason about structured information. These range from probabilistic accounts of word and concept learning to generative models that combine symbolic structure with neural inference, allowing us to derive precise, testable predictions about human behavior.
        </p>
    </div>

    {% assign a_search = site.data.areas | where: "key", "search" | first %}
    <div class="research-section" style="border-left-color: {{ a_search.color }};">
        <h4>Active learning and psychological models of uncertainty and information acquisition</h4>

        <p>Another theme of earlier, but still ongoing, work is trying to understand how humans ask questions and gather information using formal methods from optimal experimental design and Bayesian statistics. One of the tasks we use to study this is a probabilistic version of the popular code breaking game Mastermind, where the subject must guess codes that are generated from distributions over a set of items.
        </p>
    </div>
</div>
