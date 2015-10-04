import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>TubeList</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <link href='https://fonts.googleapis.com/css?family=Cantarell:400,400italic' rel='stylesheet' type='text/css'>
    <style type="text/css" media="screen">
        body {
            padding-top: 20px;
            background-color: #130400;
            font-family: 'Cantarell', italic;
        }
        .container{
            width: 100%
        }
        #trailer .modal-dialog {
            margin-top: 80px;
            width: 1280px;
            height: 720px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
            background-color: #99FF99;
        }
        #trailer-video:hover {
            width: 100%;
            height: 100%;
            background-color: #99FF99;
        }
        .movie-tile {
            margin-bottom: 5px;
            padding-top: 20px;
            padding-left: 5px;
            padding-right: 5px;
        }
        .movie-tile:hover {
            background-color: #EB5833;
            box-shadow: inset 0 0 0 10px #FFC2B2;
            transition: background-color 1.0s ease, box-shadow 0.5s ease;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: #E62E00;
        }
        .navbar-custom {
            color: #FFFFFF;
            background-color: #E62E00;
        }
        .navbar-title {
            color: #FFC2B2;
        }
        .navbar-bottom{
            height: 1.7em;
            width: 100%;
            color: #FFFFFF;
            background-color: #E62E00;
            position: fixed;
            top: 100%;
            margin-top: -2em;
        }
        .movie-title{
            color: #FFC2B2;
        }
        .square-box{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index:99;
            box-shadow: inset 0 0 0 2px #99FF99;
        }
        .square-box:hover{

            transition: box-shadow 0.5s ease;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
            $('.square-box').fadeOut().css('top', 0).css('left', 0);
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            $('.square-box').fadeIn();
            $('#box1').animate({ "left": "-15%" }, "slow" );
            $('#box2').animate({ "right": "-15%" }, "slow" );
            $('#box3').animate({ "top": "-85%" }, "slow" );
            $('#box4').animate({ "bottom": "-85%" }, "slow" );
            $('#box5').animate({ "left": "-85%" }, "slow" );
            $('#box6').animate({ "right": "-85%" }, "slow" );
            $('#box7').animate({ "top": "-15%" }, "slow" );
            $('#box8').animate({ "bottom": "-15%" }, "slow" );
            $('#box9').animate({ "left": "-50%" }, "slow" );
            $('#box10').animate({ "right": "-50%" }, "slow" );
            $('#box11').animate({ "top": "-50%" }, "slow" );
            $('#box12').animate({ "bottom": "-50%" }, "slow" );
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            })).hide();
            $("#trailer-video-container").fadeIn();
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.square-box').hide();  
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar-custom navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <span class="glyphicon glyphicon-headphones" aria-hidden="true"></span> TubeList
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <div class='square-box' id='box1'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box2'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box3'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box4'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box5'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box6'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box7'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box8'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box9'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box10'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box11'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
    <div class='square-box' id='box12'>
        <div class='square-content'><div><span>Aspect ratio 1:1</span></div></div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="480" height="360">
    <p class="movie-title">{movie_title}</p>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.link)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.link)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.image,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)