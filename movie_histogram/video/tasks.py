from analyzer.analyzer import Analyzer
from video.models import Video, Histogram


def analyze_movie(file):
    analyzer = Analyzer(file)
    video = Video.objects.create(file=file)

    for t, frame in enumerate(analyzer.get_histogram()):
        r, g, b = frame
        print("Frame:" + str(t))
        for num_bin in range(0, len(r)):
            Histogram.objects.create(video=video, t=t, num_bin=num_bin, bin_value=r[num_bin], color=Histogram.RED)
            Histogram.objects.create(video=video, t=t, num_bin=num_bin, bin_value=g[num_bin], color=Histogram.GREEN)
            Histogram.objects.create(video=video, t=t, num_bin=num_bin, bin_value=b[num_bin], color=Histogram.BLUE)
    print("Finished")
