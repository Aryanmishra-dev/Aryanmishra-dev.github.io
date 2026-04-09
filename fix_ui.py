import re

with open('index.html', 'r') as f:
    content = f.read()

# Title and Meta
content = content.replace(
    '<title>Aryan Mishra | Data Science & Tech Enthusiast</title>',
    '<title>Aryan Mishra | Data Scientist & ML Engineer</title>'
)
content = content.replace(
    'content="Aryan Mishra | Data Science & Tech Enthusiast"',
    'content="Aryan Mishra | Data Scientist & ML Engineer"'
)

# Navbar Logo
content = content.replace(
    '<div class="w-10 h-10 rounded-lg glossy-btn flex items-center justify-center">\n                        <span class="text-white font-bold text-lg">AM</span>\n                    </div>',
    '<div class="px-4 py-2 rounded-lg glossy-btn flex items-center justify-center">\n                        <span class="text-white font-bold text-lg font-mono">aryan.mishra()</span>\n                    </div>'
)

# Hero Section
content = content.replace(
    '<span class="text-gray-400 text-sm">Available for opportunities</span>',
    '<span class="text-gray-400 text-sm font-mono">available_for_internships = True</span>'
)
content = content.replace(
    'Data Science Enthusiast &<br>\n                            <span class="text-indigo-400">B.Tech Student</span>',
    'Data Scientist &<br>\n                            <span class="text-indigo-400">ML Engineer</span>'
)
content = content.replace(
    '<p class="text-gray-400 text-lg max-w-lg">\n                            Highly dedicated and hardworking individual with a strong defense background.\n                            Passionate about new and emerging technologies, with a clear drive to contribute\n                            to the nation as a technology specialist.\n                        </p>',
    '<p class="text-gray-400 text-lg max-w-lg">\n                            A data-driven problem solver specializing in machine learning, statistical modeling, and data visualization. Passionate about transforming raw data into actionable intelligence and scalable AI solutions.\n                        </p>'
)

# About Section Cards
content = content.replace(
    '<i class="fas fa-flag text-orange-400 text-xl"></i>\n                                </div>\n                                <h4 class="font-bold text-white">Defense Background</h4>\n                                <p class="text-gray-400 text-sm mt-1">Strong Values & Discipline</p>',
    '<i class="fas fa-chart-pie text-orange-400 text-xl"></i>\n                                </div>\n                                <h4 class="font-bold text-white">Data Analyst</h4>\n                                <p class="text-gray-400 text-sm mt-1">Extracting Actionable Insights</p>'
)

# About Section Text
content = content.replace(
    '<p class="text-gray-400 text-lg leading-relaxed">\n                            Currently pursuing B.Tech in Computer Science with specialization in Data Science\n                            at Indore Institute of Science and Technology. Focused on machine learning,\n                            data preprocessing, and building predictive models that solve real-world problems.\n                        </p>\n                        <p class="text-gray-400 text-lg leading-relaxed">\n                            Eager to join a major organization where my technical skills, commitment, and\n                            discipline can support India\'s advancement in the evolving era of technological\n                            warfare and innovation.\n                        </p>',
    '<p class="text-gray-400 text-lg leading-relaxed">\n                            Currently pursuing a B.Tech in Computer Science with a specialization in Data Science\n                            at Indore Institute of Science and Technology. My expertise spans the entire data\n                            lifecycle—from cleaning, wrangling, and preprocessing diverse datasets to building\n                            and deploying state-of-the-art predictive models.\n                        </p>\n                        <p class="text-gray-400 text-lg leading-relaxed">\n                            I am eager to tackle complex technical challenges, applying rigorous statistical\n                            methods and machine learning algorithms to drive strategic product decisions\n                            and create real-world impact.\n                        </p>'
)

# Skills Section
content = content.replace(
    '<h3 class="text-xl font-bold mb-3">Python Programming</h3>',
    '<h3 class="text-xl font-bold mb-3">Python for Data Science</h3>'
)

# Replace C/C++ skill with Statistical Analysis
c_cpp_block = '''<!-- C/C++ -->
                    <div class="glass-card p-8 rounded-2xl">
                        <div class="w-14 h-14 rounded-xl bg-indigo-500/15 flex items-center justify-center mb-6">
                            <i class="fas fa-code text-indigo-400 text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-bold mb-3">C / C++ Programming</h3>
                        <p class="text-gray-400 mb-6 text-sm leading-relaxed">Strong foundation in programming
                            fundamentals, data structures, and algorithms.</p>
                        <div class="skill-bar h-1.5 rounded-full">
                            <div class="skill-progress h-full rounded-full" style="width: 85%;"></div>
                        </div>
                        <span class="text-indigo-400 text-sm mt-3 inline-block font-medium">85%</span>
                    </div>'''

stats_block = '''<!-- Statistical Analysis -->
                    <div class="glass-card p-8 rounded-2xl">
                        <div class="w-14 h-14 rounded-xl bg-indigo-500/15 flex items-center justify-center mb-6">
                            <i class="fas fa-chart-line text-indigo-400 text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-bold mb-3">Statistical Analysis</h3>
                        <p class="text-gray-400 mb-6 text-sm leading-relaxed">Hypothesis testing, probability distributions, A/B testing, and exploratory data analysis.</p>
                        <div class="skill-bar h-1.5 rounded-full">
                            <div class="skill-progress h-full rounded-full" style="width: 80%;"></div>
                        </div>
                        <span class="text-indigo-400 text-sm mt-3 inline-block font-medium">80%</span>
                    </div>'''
content = content.replace(c_cpp_block, stats_block)

content = content.replace(
    '<h3 class="text-xl font-bold mb-3">SQL & Databases</h3>',
    '<h3 class="text-xl font-bold mb-3">SQL & Data Wrangling</h3>'
)

# Replace Web Development skill with Healthcare AI
web_dev_block = '''<!-- Web Development -->
                    <div class="glass-card p-8 rounded-2xl">
                        <div class="w-14 h-14 rounded-xl bg-indigo-500/15 flex items-center justify-center mb-6">
                            <i class="fab fa-react text-indigo-400 text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-bold mb-3">Web Development</h3>
                        <p class="text-gray-400 mb-6 text-sm leading-relaxed">React, HTML, CSS, Django for building
                            modern web applications.</p>
                        <div class="skill-bar h-1.5 rounded-full">
                            <div class="skill-progress h-full rounded-full" style="width: 70%;"></div>
                        </div>
                        <span class="text-indigo-400 text-sm mt-3 inline-block font-medium">70%</span>
                    </div>'''

health_ai_block = '''<!-- Healthcare AI -->
                    <div class="glass-card p-8 rounded-2xl">
                        <div class="w-14 h-14 rounded-xl bg-indigo-500/15 flex items-center justify-center mb-6">
                            <i class="fas fa-notes-medical text-indigo-400 text-2xl"></i>
                        </div>
                        <h3 class="text-xl font-bold mb-3">Healthcare AI</h3>
                        <p class="text-gray-400 mb-6 text-sm leading-relaxed">Clinical data mining, medical image analysis, and predictive healthcare modeling algorithms.</p>
                        <div class="skill-bar h-1.5 rounded-full">
                            <div class="skill-progress h-full rounded-full" style="width: 85%;"></div>
                        </div>
                        <span class="text-indigo-400 text-sm mt-3 inline-block font-medium">85%</span>
                    </div>'''
content = content.replace(web_dev_block, health_ai_block)

# Tools Replacement
old_tools = '''<div class="flex flex-wrap justify-center gap-4">
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">Python</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">C/C++</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">React</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">SQL</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">Power
                            BI</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">Tableau</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">Weka</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">Django</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">HTML/CSS</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">Excel</span>
                        <span
                            class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">Git</span>
                    </div>'''

new_tools = '''<div class="flex flex-wrap justify-center gap-4 font-mono text-sm">
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">python</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">pandas</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">numpy</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">scikit-learn</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">sql</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">power-bi</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">tableau</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">jupyter</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">colab</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">weka</span>
                        <span class="glass-card px-6 py-3 rounded-full text-gray-400 hover:text-indigo-400 hover:border-indigo-500 transition-all cursor-default">git</span>
                    </div>'''
content = content.replace(old_tools, new_tools)


# Projects Section
content = content.replace(
    '<div class="flex items-center gap-2 mb-3">\n                                <span class="text-xs bg-indigo-500/20 text-indigo-400 px-3 py-1 rounded-full">Machine\n                                    Learning</span>\n                                <span\n                                    class="text-xs bg-green-500/20 text-green-500 px-3 py-1 rounded-full">Python</span>\n                            </div>',
    '<div class="flex flex-wrap items-center gap-2 mb-3 font-mono">\n                                <span class="text-xs bg-indigo-500/20 text-indigo-400 px-3 py-1 rounded-full">scikit-learn</span>\n                                <span class="text-xs bg-blue-500/20 text-blue-400 px-3 py-1 rounded-full">pandas</span>\n                                <span class="text-xs bg-green-500/20 text-green-500 px-3 py-1 rounded-full">Python</span>\n                            </div>'
)

content = content.replace(
    '<div class="flex items-center gap-2 mb-3">\n                                <span class="text-xs bg-purple-500/20 text-purple-500 px-3 py-1 rounded-full">Healthcare\n                                    AI</span>\n                                <span class="text-xs bg-green-500/20 text-green-500 px-3 py-1 rounded-full">Live\n                                    Demo</span>\n                            </div>',
    '<div class="flex flex-wrap items-center gap-2 mb-3 font-mono">\n                                <span class="text-xs bg-purple-500/20 text-purple-500 px-3 py-1 rounded-full">medical-datasets</span>\n                                <span class="text-xs bg-indigo-500/20 text-indigo-400 px-3 py-1 rounded-full">predictive-modeling</span>\n                                <span class="text-xs bg-green-500/20 text-green-500 px-3 py-1 rounded-full">Python</span>\n                            </div>'
)

content = content.replace(
    '<i class="fas fa-external-link-alt"></i> View on Colab',
    '<i class="fas fa-external-link-alt"></i> open_in_colab()'
)
content = content.replace(
    '<i class="fas fa-external-link-alt"></i> View Live Demo',
    '<i class="fas fa-external-link-alt"></i> view_live_demo()'
)

content = re.sub(
    r'class="glossy-btn px-6 py-2 rounded-full text-white text-sm inline-flex items-center gap-2"',
    r'class="glossy-btn px-6 py-2 rounded-full text-white text-sm inline-flex items-center gap-2 font-mono w-max"',
    content
)

content = content.replace(
    '<i class="fab fa-github"></i> View All on GitHub',
    '<i class="fab fa-github"></i> view_all()'
)
content = content.replace(
    'class="glossy-btn px-8 py-3 rounded-full text-white font-medium inline-flex items-center gap-2"',
    'class="glossy-btn px-8 py-3 rounded-full text-white font-medium inline-flex items-center gap-2 font-mono"'
)


# Footer
content = content.replace(
    '<footer class="glass-card border-t border-white/10 py-8">',
    '<footer class="glass-card border-t border-white/10 py-8 font-mono">'
)

with open('index.html', 'w') as f:
    f.write(content)
