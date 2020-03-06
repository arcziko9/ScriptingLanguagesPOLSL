import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import org.jfree.chart.*;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.CategoryDataset;
import org.jfree.data.category.DefaultCategoryDataset;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

public class Rowerzysta {
    public JFreeChart createChart(int height, int width, String chartTitle, List<Double> radiusValues, List<Double> distanceValues, List<Double> resultValues) {
        JFreeChart barChart = ChartFactory.createBarChart(
                chartTitle,
                "Category",
                "Score",
                createDataset(radiusValues, distanceValues, resultValues),
                PlotOrientation.VERTICAL,
                true, true, false);
        ChartPanel chartPanel = new ChartPanel(barChart);
        chartPanel.setPreferredSize(new java.awt.Dimension(width , height));

        return barChart;
    }

    private CategoryDataset createDataset(List<Double> radiusValues, List<Double> distanceValues, List<Double> resultValues) {
        int length = radiusValues.size();
        final DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        String label1 = "";
        String label2 = "";
        String label3 = "";

        for(int i = 0; i < length; i++) {
            label1 = "Radius" + Integer.toString(i);
            label2 = "Distance" + Integer.toString(i);
            label3 = "Results" + Integer.toString(i);
            dataset.addValue(radiusValues.get(i), label1, "Radius");
            dataset.addValue(distanceValues.get(i), label2, "Distance");
            dataset.addValue(resultValues.get(i), label3, "Results");
        }
        return dataset;
    }

    public double getX(double r, double t) {
        return r * (t - Math.sin(t));
    }

    public double getY(double r, double t) {
        return r * (1 - Math.cos(t));
    }

    public double getResult(double radius, double distance) {
        double x1 = 0, x2; // współrzędne x położenia muchy
        double y1 = 0, y2; // współrzędne y położenia muchy
        double t = 0;
        double result = 0;
        while (x1 < distance) {
            x2 = getX(radius, t);
            y2 = getY(radius, t);
            result += Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
            x1 = x2;
            y1 = y2;
            t += 0.01; // zwiększenie kata o stala wartosc 0.01rad
        }
        return result;
    }

    public void writeResultToFile(double result, String outputFileName) throws FileNotFoundException {
        PrintWriter out = new PrintWriter("./output/" + outputFileName);
        String output = Double.toString(result);
        out.write(output);
        out.close();
    }

    public File[] getFilesInDirectory(String pathInput) {
        File dir = new File(pathInput);
        File[] filesInDirectory = dir.listFiles();
        return filesInDirectory;
    }

    public static String getStringDate() {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy_MM_dd");
        LocalDateTime now = LocalDateTime.now();
        String date = dtf.format(now);
        return date;
    }

    public static void main(String[] args) throws FileNotFoundException, IOException {
        Rowerzysta rowerzysta = new Rowerzysta();
        String pathInput = "./input/";
        File[] filesInDirectory = rowerzysta.getFilesInDirectory(pathInput);
        List<Double> radiusValues = new ArrayList<Double>();
        List<Double> distanceValues = new ArrayList<Double>();
        List<Double> resultsValues = new ArrayList<Double>();

        int count = 0;
        for(File f : filesInDirectory) {
            File file = new File(pathInput + f.getName());
            Scanner in = new Scanner(file);
            try{
                double radius = 0;
                double distance = 0;
                double result = 0;
                while(in.hasNext()) {
                       radius = in.nextDouble();
                       distance = in.nextDouble();
                    result = rowerzysta.getResult(radius, distance);
                    radiusValues.add(radius);
                    distanceValues.add(distance);
                    resultsValues.add(result);
                    count++;
                    String outputFileName = "output_" + count + ".txt";
                    rowerzysta.writeResultToFile(result, outputFileName);
                }
            } catch (Exception e) {
                System.out.println("Error: " + e);
            }
            in.close();
        }
        JFreeChart chart = rowerzysta.createChart(650, 600, "Chart", radiusValues, distanceValues, resultsValues);
        ChartUtilities.saveChartAsJPEG(new File("./images/chart_" + getStringDate() + ".png"), chart, 600, 650);
    }
}
