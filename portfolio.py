#!/usr/bin/python3
import os

PATH = os.path.dirname(__file__)

fname = input('First name: ')
lname = input('Last name: ')
description = input('Short description of yourself: ')

experience_num = 0
if experience_input := input('Number of job/experience items: '):
    experience_num = int(experience_input)
experience_content = ''
for i in range(experience_num):
    experience_title = input('Job/experience title: ')
    experience_duration = input('Job/experience duration: ')
    experience_description = input('Job/experience description: ')
    experience_content += f'<li>\n<h3>{experience_title}</h3>\n<h4 class="lead">{experience_duration}</h4>\n<p>{experience_description}</p>\n</li>\n'

project_num = 0
if project_input := input('Number of projects: '):
    project_num = int(project_input)
project_rows = project_num // 3 + project_num % 3
project_content = ''
for i in range(project_rows):
    project_content += '<div class="row text-center">\n'
    for j in range(project_num):
        project_title = input(f'Project {j*3+i+1} title: ')
        project_description = input(f'Project {j*3+i+1} description: ')
        project_url =  input(f'Project {j*3+i+1} URL: ')
        project_content += f'<div class="col-md-4 my-2">\n<div class="card">\n<div class="card-body">\n<h3 class="card-title">{project_title}</h3>\n<p class="card-text lead">{project_description}</p>\n<a href="{project_url}" target="_blank" class="btn btn-primary">Check it out</a>\n</div>\n</div>\n</div>\n'
    project_content += '</div>\n'
portriat_url = input('Portriat URL: ')

print('Enter a blank line if you do not use one of the following platforms')
contact_content = ''
if email := input('Email: '):
    contact_content += f'<li><a href="mailto:{email}" target="_blank"><i class="bi bi-envelope me-3"></i></a></li>\n'
if linkedin := input('Linkedin URL: '):
    contact_content += f'<li><a href="{linkedin}" target="_blank"><i class="bi bi-linkedin me-3"></i></a></li>\n'
if github := input('Github URL: '):
    contact_content += f'<li><a href="{github}" target="_blank"><i class="bi bi-github me-3"></i></a></li>\n'
if twitter := input('Twitter URL: '):
    contact_content += f'<li><a href="{twitter}" target="_blank"><i class="bi bi-twitter me-3"></i></a></li>\n'

print('Enter hex color codes for the following prompts. You can use https://www.canva.com/colors for some inspiration. Enter a blank line for the default colors.')
if body_primary := input('Primary body text: ') == '':
    body_primary = '#343a40'
if bg_primary := input('Primary background: ') == '':
    bg_primary = '#FFFFF0'
if bg_secondary := input('Secondary background: ') == '':
    bg_secondary = '#F1E4D1'
if header_primary := input('Primary header: ') == '':
    header_primary = '#7373FF'
if header_secondary := input('Secondary header: ') == '':
    header_secondary = '#3479d3'
if nav_accent := input('Navbar accent: ') == '':
    nav_accent = '#F0F0FF'
if hover := input('Link hovering color: ') == '':
    hover = '#7373FF'
if accent := input('Accent for portrait and left border on experience items: ') == '':
    accent = '#FF6FB7'

content = f'''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <title>{fname} {lname}'s Portfolio</title>
    </head>
    <!--CSS styling-->
    <style>
        /*General shit*/
        :root{{
            --body-primary: {body_primary};
            --bg-primary: {bg_primary};
            --bg-secondary: {bg_secondary};
            --header-primary: {header_primary};
            --header-secondary: {header_secondary};
            --nav-accent: {nav_accent};
            --hover: {hover};
            --accent: {accent};
        }}
        body{{
            transition: opacity 1.5s;
            background-color: var(--bg-primary);
            opacity: 0;
        }}
        p, a, h1, h2, h3, h4, h5, h6{{
            color: var(--body-primary);
        }}
        section{{
            /*height: 100vh;*/
            padding: 20px 0;
        }}
        .fadein{{
            opacity: 0;
        }}
        .heading{{
            color: var(--header-primary)
        }}
        .card-title{{
            color: var(--header-secondary)
        }}
        /*Navbar*/
        .navbar{{
            position: sticky;
            top: 0;
            width: 100%;
            background-color: transparent;
        }}
        .navbar ul{{
            text-align: center;
        }}
        .nav-item{{
            display: inline;
        }}
        .nav-item a{{
            transition: 0.5s;
            font-size: 1.5rem;
            text-decoration: none;
            color: var(--body-primary);
            border-bottom: 3px solid var(--nav-accent);
        }}
        .nav-item a:hover{{
            transition: 0.5s;
            border-bottom: 3px solid var(--hover);
        }}
        /*Waving animation*/
        .wave{{
            animation-name: wave-animation;
            animation-duration: 2s;
            animation-iteration-count: infinite;
            transform-origin: 70% 70%;
            display: inline-block;
        }}
        @keyframes wave-animation{{
            0% {{transform: rotate( 0.0deg)}}
            10% {{transform: rotate(14.0deg)}}
            20% {{transform: rotate(-8.0deg)}}
            30% {{transform: rotate(14.0deg)}}
            40% {{transform: rotate(-4.0deg)}}
            50% {{transform: rotate(10.0deg)}}
            60% {{transform: rotate( 0.0deg)}}
            100% {{transform: rotate( 0.0deg)}}
        }}
        /*Home section*/
        .about-me{{
            font-size: 1.5rem;
        }}
        .contact-items li{{
            display: inline-block;
        }}
        .contact-items a{{
            transition: 0.5s;
            text-decoration: none;
            font-size: 2rem;
            display: inline-block;
        }}
        .contact-items a:hover{{
            transition: 0.5s;
            color: var(--hover)
        }}
        .rounded-circle{{
            border: 3px solid var(--accent);
        }}
        /*Experience section*/
        #experience{{
            background-color: var(--bg-secondary);
        }}
        .experience-items li{{
            border-left: 5px solid var(--accent);
            padding-left: 20px;
        }}
        .experience-items li h3{{
            color: var(--header-secondary);
        }}
    </style>
    <!--Body of site-->
    <body onload="document.body.style.opacity='1'">
        <!--Navbar-->
        <div class="navbar justify-content-center">
            <ul class="m-0 p-0 list-unstyled text-unstyled">
                <li class="nav-item mx-2">
                    <a href="#"><i class="bi bi-house-door"></i></a>
                </li>
                <li class="nav-item mx-2">
                    <a href="#experience"><i class="bi bi-hourglass"></i></a>
                </li>
                <li class="nav-item mx-2">
                    <a href="#projects"><i class="bi bi-code-slash"></i></a>
                </li>
            </ul>
        </div>
        <!--Home section-->
        <section id="home" class="p-4">
            <div class="container">
                <h1 class="mb-3 heading"><span class="wave">👋</span> Hi, my name is {fname} {lname}</h1>
                <div class="row">
                    <div class="col-md-8">
                        <p class="lead about-me">{description}</p>
                        <ul class="contact-items list-unstyled">
                            {contact_content}
                        </ul>
                    </div>
                    <div class="col-md-4 text-center">
                        <img class="rounded-circle p-2" src="{portriat_url}" width="100%">
                    </div>
                </div>
            </div>
        </section>
        <!--Experience section-->
        <section id="experience" class="p-4">
            <div class="container">
                <h1 class="mb-3 heading">Experience</h1>
                <ul class="experience-items m-0 p-0 list-unstyled">
                    {experience_content}
                </ul>
            </div>
        </section>
        <!--Projects section-->
        <section id="projects" class="p-4">
            <div class="container">
                <h1 class="mb-3 heading">Projects</h1>
                {project_content}
            </div>
        </section>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    </body>
</html>
'''

with open(os.path.join(PATH,'output.html'), 'wb') as f:
    f.write(content.encode())