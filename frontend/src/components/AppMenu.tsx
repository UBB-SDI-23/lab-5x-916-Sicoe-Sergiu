import {Box, AppBar, Toolbar, IconButton, Typography, Button, Container} from "@mui/material";
import {Link, useLocation} from "react-router-dom";
import CarIcon from "@mui/icons-material/CarRental";
import Car from "@mui/icons-material/CarRentalRounded";
import {useState} from "react";
import {Star} from "@mui/icons-material";
import { AllEventFounders} from "./EventFounders/allEventFounders";

export const AppMenu = () => {
    const location = useLocation();
    const path = location.pathname;
    const [state, setState] = useState(0);

    return (
        <Container>
            {state === 0 && (
                <Box sx={{flexGrow: 1}}>
                    <AppBar position="static" sx={{marginBottom: "20px"}}>
                        <Toolbar>
                            <IconButton
                                component={Link}
                                to="/"
                                size="large"
                                edge="start"
                                color="inherit"
                                aria-label="school"
                                sx={{mr: 2}}>
                                <CarIcon/>
                            </IconButton>
                            <Typography variant="h6" component="div" sx={{mr: 5}}>
                                Artist Managers management
                            </Typography>
                            <Button
                                to="/"
                                component={Link}
                                color="inherit"
                                sx={{mr: 5}}
                                startIcon={<Car/>}
                                onClick={() => setState(1)}
                            >
                                Artist Managers
                            </Button>
                        </Toolbar>
                        <Toolbar>
                            <IconButton
                                component={Link}
                                to="/"
                                size="large"
                                edge="start"
                                color="inherit"
                                aria-label="school"
                                sx={{mr: 2}}>
                                <Star/>
                            </IconButton>
                            <Typography variant="h6" component="div" sx={{mr: 5}}>
                                Statistics:
                            </Typography>
                            <Button
                                to="/"
                                component={Link}
                                color="inherit"
                                sx={{mr: 5}}
                                startIcon={<Star/>}
                                onClick={() => setState(2)}
                            >
                                Statistics
                            </Button>
                        </Toolbar>
                    </AppBar>
                </Box>
            )}
            {/*{state === 1 && (*/}
            {/*    <><Button*/}
            {/*        to="/"*/}
            {/*        component={Link}*/}
            {/*        color="inherit"*/}
            {/*        sx={{mr: 5}}*/}
            {/*        startIcon={<Car/>}*/}
            {/*        onClick={() => setState(0)}*/}
            {/*    >*/}
            {/*        Back*/}
            {/*    </Button><allEventFounders/></>*/}
            {/*)}*/}
            {/*{state === 2 && (*/}
            {/*    <><Button*/}
            {/*        to="/"*/}
            {/*        component={Link}*/}
            {/*        color="inherit"*/}
            {/*        sx={{mr: 5}}*/}
            {/*        startIcon={<Car/>}*/}
            {/*        onClick={() => setState(0)}*/}
            {/*    >*/}
            {/*        Back*/}
            {/*    </Button><Statistic1/></>*/}
            {/*)}*/}
        </Container>
    );
};