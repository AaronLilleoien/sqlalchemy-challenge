import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
#List all available routes
@app.route("/")
def main():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"api/v1.0/start/end"

    )

#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    #session = Session(engine)
    prv_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prv_year).all()
    session.close()

    precip = { date: prcp for date, prcp in precipitation}

    return jsonify(precip)

app.route("/api/v1.0/stations")
def station():
    session = Session(engine)
    distinct_stations = session.query(Measurement.station).distinct().all()
    session.close
    stations =list(np.ravel(results))
    return jsonify(stations=stations)

#app.route("/api/v1.0/tobs")
#def tobs():
 #   return()



#app.route("/api/v1.0/<start>")
#def start():
 #   return()


#app.route("/api/v1.0/<start>/<end>")
#def start_end():
 #   return()




if __name__ == '__main__':
    app.run(debug=True)